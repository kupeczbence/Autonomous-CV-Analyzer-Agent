import streamlit as st
from transformers import pipeline
from src.agent import run_cv_agent

st.title("Autonomous CV Analyzer Agent")


@st.cache_resource
def load_llm():
    return pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        return_full_text=False,
        max_new_tokens=100,
        temperature=0.1,
    )


cv_file = st.file_uploader("Upload CV (PDF)")
job_text = st.text_area("Paste job description")

if st.button("Analyze") and cv_file and job_text:

    with open("temp.pdf", "wb") as f:
        f.write(cv_file.read())

    llm = load_llm()

    result = run_cv_agent(llm, "temp.pdf", job_text)

    st.subheader("CV Skills")
    st.write(result["cv_skills"])

    st.subheader("Job Skills")
    st.write(result["job_skills"])

    st.subheader("Match Score")
    st.progress(result["score"])

    st.write(f"Score: {result['score']*100:.1f}%")

    with st.expander("Debug"):
        st.text(result["raw_job_output"])