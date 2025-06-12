# 🧠 NoteGenie – Summarize Notes & Create Quizzes (Free AI Tool)

NoteGenie is a simple yet powerful Gen-AI tool designed for students to **summarize long notes** and **generate quiz questions** instantly. Built using **Streamlit** and **HuggingFace Transformers**, this tool runs entirely free – no OpenAI API or paid keys required!

---

## ✨ Features

- 🔍 Summarizes lengthy text notes in one click  
- ❓ Creates 3-question quizzes based on your notes  
- ✅ Completely free using HuggingFace models  
- 💡 Beginner-friendly and easy to run locally

---

## 🚀 How It Works

1. Paste your notes into the text area  
2. Click “Summarize” – generates a short summary  
3. Click “Generate Quiz” – turns lines into quiz questions  
4. See results right in the app

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- HuggingFace Transformers (`pipeline("summarization")`)

---

## 🧑‍💻 How to Run Locally

```bash
git clone https://github.com/your-username/NoteGenie.git
cd NoteGenie
pip install -r requirements.txt
streamlit run app.py
