# **QwenRAG - Retrieval-Augmented Generation with FAISS & Ollama**

QwenRAG is a **free and open-source Retrieval-Augmented Generation (RAG) application** that leverages **FAISS** for vector storage and **Ollama** for LLM inference using the `qwen2.5:0.5b` model. This project allows efficient document retrieval and AI-generated responses.

---

## **🚀 Features**
- Uses **FAISS** for fast similarity search
- Runs **Qwen2.5-0.5B** model locally via **Ollama**
- Accepts user queries and retrieves relevant documents
- Generates AI-based responses using the retrieved context
- No paid API required — **fully local & open-source!**

---

## **📂 Project Structure**
```
QwenRAG/
│── data/                # Folder containing text documents
│   ├── sample.txt       # Example document
│── faiss_index.bin      # FAISS vector index file
│── doc_ids.npy          # Document ID mapping for FAISS
│── retrieve.py          # Document retrieval logic
│── generate.py          # AI response generation using Ollama
│── README.md            # Project documentation
```

---

## **🛠️ Installation & Setup**

### **1️⃣ Install Dependencies**
Make sure you have **Python 3.10+**, `pip`, and `git` installed. Then, install the required Python packages:
```sh
pip install faiss-cpu numpy sentence-transformers ollama
```

### **2️⃣ Install & Run Ollama**
1. **Install Ollama** (if not installed):
   ```sh
   iwr https://ollama.com/install.ps1 -useb | iex   # Windows
   curl -fsSL https://ollama.com/install.sh | sh   # Linux/macOS
   ```
2. **Pull the Qwen2.5-0.5B model:**
   ```sh
   ollama pull qwen2.5:0.5b
   ```
3. **Verify Ollama is working:**
   ```sh
   ollama run qwen2.5:0.5b
   ```

---

## **📌 How to Use**

### **1️⃣ Index Documents**
Ensure that your documents are inside the `data/` folder. If needed, modify `retrieve.py` to load your own text files.

### **2️⃣ Retrieve Relevant Documents**
Run the retrieval script:
```sh
python retrieve.py
```
This script loads the FAISS index and retrieves documents based on user queries.

### **3️⃣ Generate AI Responses**
Once documents are retrieved, use the `generate.py` script to generate responses:
```sh
python generate.py
```

---

## **💡 Example Usage**
### **Retrieval (`retrieve.py`)**
```sh
Query: "What is machine learning?"
Retrieved Documents: ["Machine learning is a field of AI that allows computers to learn patterns from data..."]
```

### **Generation (`generate.py`)**
```sh
Generated Response: "Machine learning is a branch of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed..."
```

---

## **🤖 Future Improvements**
✅ Add a web UI using **Streamlit**
✅ Support multi-file document ingestion
✅ Implement a chatbot interface

---

## **📝 License**
This project is licensed under the **MIT License**.

---

## **👨‍💻 Contributing**
Pull requests are welcome! Feel free to submit issues or suggest improvements.

**Happy Coding! 🚀**

