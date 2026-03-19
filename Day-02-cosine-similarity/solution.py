# Day 02 - Cosine Similarity


import math
import numpy as np


# Traditional Approach
def cosine_similarity_traditional(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(a * a for a in v1))
    magnitude_v2 = math.sqrt(sum(b * b for b in v2))
    
    return dot_product / (magnitude_v1 * magnitude_v2)


# Pythonic Approach
def cosine_similarity_pythonic(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    cosine_similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return float(cosine_similarity)


if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [5, -1, 7]

    print("Input Vectors:")
    print("v1 =", v1)
    print("v2 =", v2)
    print()

    print("Cosine Similarity Results:")
    print("Traditional:", cosine_similarity_traditional(v1, v2))
    print("Pythonic:", cosine_similarity_pythonic(v1, v2))