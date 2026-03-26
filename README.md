# Autonomous CV Analyzer Agent

An AI-powered agent that automatically analyzes a CV against a job description, extracts skills from both and computes a match score.

The system combines:
- deterministic parsing
- LLM-based information extraction
- and rule-based scoring

---

## Features

- Upload CV in **PDF format**
- Paste job description
- Extracts:
  - CV skills
  - Job-required skills
- Calculates a **match percentage**
- Includes fallback logic if the LLM fails

---

## Demo Workflow

1. Upload CV
2. Paste job description
3. Click **Analyze**
4. View:
   - extracted skills
   - match score
   - debug LLM output

---

## Project Structure

```
project-root/
│
├── app.py                 # Streamlit UI
├── src/
│   ├── agent.py           # Orchestrates the pipeline
│   ├── tools.py           # Skill extraction + prompt logic
│   ├── parsing.py         # PDF text extraction
│   └── scoring.py         # Skill matching algorithm
```

---
## Why This Is an Agentic AI System

This project is not a simple LLM application. It implements an **agentic architecture**, where the language model is used as one component in a multi-step decision pipeline.

The agent:
1. Receives a task (CV + job description)
2. Uses multiple tools to gather information
3. Decides how to proceed based on intermediate results
4. Applies fallback strategies when necessary

This mirrors real-world autonomous AI systems that:
- orchestrate tools
- perform conditional reasoning
- and execute multi-step workflows.
---

## How It Works

### 1. CV Parsing
The system extracts text from the uploaded PDF:

```
parsing.py → extract_text_from_cv()
```

### 2. CV Skill Extraction
A deterministic regex parser searches the **SKILLS** section.

```
tools.py → extract_skills_from_section()
```

### 3. Job Skill Extraction (LLM)
A prompt-driven LLM extracts required skills from the job description.

Model used:
```
TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

### 4. Fallback Logic
If the LLM returns empty output, a rule-based keyword search is used.

### 5. Match Scoring
The final score is calculated as:

```
matches / required_skills
```

Implemented in:
```
scoring.py → compute_match_score()
```

---

## Installation

### 1. Create environment

```
conda create -n cv-agent python=3.10
conda activate cv-agent
```

### 2. Install dependencies

```
install the requirements.txt
```

---

## Running the App

```
streamlit run app.py
```

Then open in browser:

```
Usually it automatically opens up in browser or click: http://localhost:.....
```

---

## Example Input

### CV
- Uploaded as PDF

### Job Description
```
Skills:
Must include Java and LLMs.
Languages:
English and Hungarian.
```

---

## Test results

<img width="1912" height="898" alt="CVAgent 1" src="https://github.com/user-attachments/assets/1961aa21-acdf-4a10-8db8-257f858ab38d" />

<img width="1913" height="900" alt="CVAgent 2" src="https://github.com/user-attachments/assets/a487ded5-63dd-4513-950b-65fb1246e7da" />

<img width="1905" height="547" alt="CVAgent 3" src="https://github.com/user-attachments/assets/b6930692-dcb1-480d-b9ab-b58f44c6a0cd" />

---
## Technologies Used

- **Streamlit** – web interface
- **Transformers** – language model inference
- **TinyLlama** – lightweight LLM
- **LangChain PromptTemplate** – prompt management
- **PyPDF** – CV parsing

---

## Limitations

- CV must contain a clearly labeled **SKILLS** section
- LLM extraction quality depends on the job description structure
- Skill matching is string-based (no embeddings)

---

## Future Improvements

- Embedding-based skill similarity
- Named entity recognition for skills
- Multi-language CV support
- Web deployment

---

## Author

- LinkedIn: www.linkedin.com/in/bence-kupecz-119701305
- GitHub: https://github.com/kupeczbence
