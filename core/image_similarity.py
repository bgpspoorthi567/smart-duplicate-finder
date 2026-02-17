from PIL import Image
import imagehash


def compute_phash(image_path):
    try:
        img = Image.open(image_path)
        return imagehash.phash(img)
    except:
        return None


def is_similar(hash1, hash2, threshold=5):
    return abs(hash1 - hash2) <= threshold
