from embedder import Embedder

embedder = Embedder("models/Xenova/all-MiniLM-L6-v2")

query = "How does approximate nearest neighbor search work?"

embedding = embedder.encode(query)

print(f"Embedding dimension: {len(embedding)}")
print(f"First value: {embedding[0]}")