from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_text_similarity(text1, text2):
    embeddings = model.encode([text1, text2])
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )
    return float(similarity[0][0])
