import streamlit as st
import os

from core.scanner import scan_folder
from core.hashing import sha256_hash
from core.image_similarity import compute_phash, is_similar
from core.text_similarity import compute_text_similarity
from core.analytics import calculate_storage_saved
from core.file_actions import delete_file, move_file
from core.adaptive_threshold import get_threshold


st.set_page_config(layout="wide")
st.title("Smart Duplicate File Finder")

folder = st.text_input("Enter folder path to scan", ".")

if st.button("Run Scan"):

    if not os.path.exists(folder):
        st.error("Invalid folder path.")
        st.stop()

    files = scan_folder(folder)
    duplicates = []

    # -----------------------------
    # Exact Duplicate Detection
    # -----------------------------
    st.subheader("Exact Duplicates")
    hash_map = {}

    for file in files:
        file_hash = sha256_hash(file)
        if not file_hash:
            continue

        if file_hash in hash_map:
            duplicates.append(file)
            st.write(file)
        else:
            hash_map[file_hash] = file

    # -----------------------------
    # Image Similarity Detection
    # -----------------------------
    st.subheader("Similar Images")
    image_hashes = {}

    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            phash = compute_phash(file)
            if not phash:
                continue

            for existing_hash, existing_file in image_hashes.items():
                if is_similar(phash, existing_hash):
                    duplicates.append(file)
                    st.write(f"{existing_file}  <->  {file}")
                    break
            else:
                image_hashes[phash] = file

    # -----------------------------
    # Text Similarity Detection
    # -----------------------------
    st.subheader("Similar Text Files")
    texts = {}
    similarity_scores = []

    for file in files:
        if file.lower().endswith(".txt"):
            try:
                content = open(file, encoding="utf-8", errors="ignore").read()
            except:
                continue

            for old_file, old_content in texts.items():
                score = compute_text_similarity(old_content, content)
                similarity_scores.append(score)
                threshold = get_threshold(similarity_scores)

                if score > threshold:
                    duplicates.append(file)
                    st.write(f"{old_file}  <->  {file}  (Score: {round(score,2)})")
                    break
            else:
                texts[file] = content

    # -----------------------------
    # Storage Analysis
    # -----------------------------
    if duplicates:
        saved = calculate_storage_saved(duplicates)
        st.subheader("Storage Analysis")
        st.write(f"Recoverable Storage: {round(saved, 2)} MB")
    else:
        st.info("No duplicates found.")

    # -----------------------------
    # Cleanup Section
    # -----------------------------
    if duplicates:
        st.subheader("Cleanup Options")

        for i, file in enumerate(duplicates):
            col1, col2 = st.columns(2)

            with col1:
                if st.button("Delete", key=f"delete_{i}"):
                    delete_file(file)
                    st.success(f"Deleted {file}")

            with col2:
                if st.button("Move to Backup", key=f"move_{i}"):
                    move_file(file)
                    st.success(f"Moved {file} to duplicates_backup")

    st.success("Scan completed.")
