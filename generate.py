import ollama

def generate_response(context, query):
    prompt = f"Answer this based on the following context:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    
    response = ollama.chat(model="qwen2.5:0.5b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

# Example usage
query = "Explain machine learning basics."
context = "Machine learning is a field of AI that allows computers to learn patterns from data..."
response = generate_response(context, query)
print("Generated Response:", response)

