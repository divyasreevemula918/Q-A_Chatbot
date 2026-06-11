# 🤖 Q&A Chatbot

An intelligent Question & Answer Chatbot built using Large Language Models (LLMs) that provides accurate and context-aware responses to user queries. The application offers an interactive chat interface and leverages modern AI technologies for natural language understanding and response generation.

## 🚀 Features

- 💬 Interactive chat interface
- 🤖 LLM-powered question answering
- 📚 Context-aware responses
- ⚡ Fast and efficient query processing
- 🎨 User-friendly UI with Streamlit
- 🔍 Retrieval-Augmented Generation (RAG) support
- 🧠 Conversation memory for better interactions
- 🔐 Secure API key management using environment variables

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq / Gemini / OpenAI APIs
- FAISS / ChromaDB (if applicable)
- Hugging Face Embeddings
- Vector Database
- Retrieval-Augmented Generation (RAG)

## 📂 Project Structure

```bash
Q-A_Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── data/
├── vectorstore/
├── utils/
├── images/
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/divyasreevemula918/Q-A_Chatbot.git
cd Q-A_Chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root and add:

```env
GROQ_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

## 📸 Demo



### Home Page

![Home Page](images/home.png)

### Chat Interface

![Chat Interface](images/chat.png)

## 🎯 How It Works

1. User enters a question.
2. The chatbot processes the query.
3. Relevant context is retrieved from the knowledge base.
4. The LLM generates an accurate response.
5. The answer is displayed in the chat interface.

## 📈 Key Highlights

- Improved response accuracy using RAG architecture.
- Reduced hallucinations through contextual retrieval.
- Supports real-time conversational interactions.
- Scalable architecture for custom knowledge bases.

## 🔮 Future Enhancements

- Voice-based interaction
- Multi-language support
- PDF and document upload
- Advanced conversation memory
- Authentication and user management

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License.

## 👩‍💻 Author

**Divyasree Vemula**

GitHub: https://github.com/divyasreevemula918

---
