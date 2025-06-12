import streamlit as st
from transformers import pipeline

# Load summarizer from HuggingFace
summarizer = pipeline("summarization")

# Simple quiz generator (placeholder logic)
def generate_quiz(text):
    questions = []
    lines = text.strip().split('.')
    for i, line in enumerate(lines[:3]):
        if len(line.strip()) > 10:
            q = f"What is the main idea of: '{line.strip()}...'"
            questions.append(f"{i+1}. {q}\n(a) Option A\n(b) Option B\n(c) Option C\n")
    return "\n".join(questions)

# Streamlit UI
st.set_page_config(page_title="NoteGenie - Free Version", layout="centered")
st.title("🧠 NoteGenie - Summarize Notes & Create Quizzes (Free Version)")
st.markdown("Paste your notes below:")

user_input = st.text_area("📝 Your Notes", height=300)

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Summarize"):
        if user_input.strip():
            with st.spinner("Summarizing..."):
                summary = summarizer(user_input, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
                st.subheader("📄 Summary")
                st.write(summary)
        else:
            st.warning("Please enter some notes first.")

with col2:
    if st.button("❓ Generate Quiz"):
        if user_input.strip():
            with st.spinner("Generating questions..."):
                quiz = generate_quiz(user_input)
                st.subheader("🧩 Quiz")
                st.write(quiz)
        else:
            st.warning("Please enter some notes before generating quiz.")

st.markdown("---")
st.caption("🚀 Free AI by Team Alvengers – Hrishita, Parag, Ritu & Soumya")
