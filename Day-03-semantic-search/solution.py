# Day 03 - Semantic Search
# Demonstrates keyword search vs semantic search using embeddings

from sentence_transformers import SentenceTransformer, util


# 🔹 Traditional Keyword Search
def keyword_search(text, query):
    """
    Returns True if query is found in text (exact match)
    """
    return query.lower() in text.lower()


# 🔹 Semantic Similarity
def compute_similarity(s1, s2, model):
    """
    Compute cosine similarity between two sentences
    """
    v1 = model.encode(s1)
    v2 = model.encode(s2)

    return float(util.cos_sim(v1, v2))


# 🔹 Semantic Search
def semantic_search(query, documents, model):
    """
    Finds the most similar document to the query
    """
    doc_embeddings = model.encode(documents)
    query_embedding = model.encode(query)

    scores = util.cos_sim(query_embedding, doc_embeddings)

    best_index = scores[0].argmax().item()
    best_score = float(scores[0][best_index])

    return documents[best_index], best_score


if __name__ == "__main__":
    # Load model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 🔹 Example 1: Keyword search failure
    text = "I bought a new sofa yesterday"
    query = "couch"

    print("Keyword Search:")
    print(f"Query: {query}")
    print(f"Text: {text}")
    print("Match Found:", keyword_search(text, query))
    print()

    # 🔹 Example 2: Semantic similarity
    s1 = "The weather is freezing"
    s2 = "It is very cold outside"

    similarity = compute_similarity(s1, s2, model)

    print("Semantic Similarity:")
    print(f"Sentence 1: {s1}")
    print(f"Sentence 2: {s2}")
    print(f"Similarity Score: {similarity:.4f}")
    print()

    # 🔹 Example 3: Semantic search
    query = "I love AI"

    documents = [
        "AI is not good",
        "I enjoy machine learning",
        "The sky is nice",
        "I love Artificial Intelligence"
    ]

    best_match, score = semantic_search(query, documents, model)

    print("Semantic Search:")
    print(f"Query: {query}")
    print(f"Best Match: {best_match}")
    print(f"Score: {score:.4f}")