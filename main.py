from retrieve import retrieve_relevant_docs
from generate import generate_response

query = input("Enter your query: ")
retrieved_docs = retrieve_relevant_docs(query)
context = "\n".join(retrieved_docs)

response = generate_response(context, query)
print("Final RAG Response:", response)
