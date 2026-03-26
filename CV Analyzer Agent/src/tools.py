import re
from langchain_core.prompts import PromptTemplate

# CV SECTION PARSER 

def extract_skills_from_section(cv_text: str):
    match = re.search(
        r"SKILLS(.*?)(EDUCATION|LANGUAGES|WORK EXPERIENCE|$)",
        cv_text,
        re.S | re.I
    )

    if not match:
        return []

    skills_block = match.group(1)

    lines = [l.strip() for l in skills_block.split("\n") if l.strip()]

    skills = []
    for line in lines:
        if len(line.split()) <= 3:
            skills.append(line.lower())

    return list(set(skills))


# LLM JOB EXTRACTION

JOB_PROMPT = PromptTemplate.from_template("""
You are an information extraction system.

Extract only the required skills and languages from the job description.

Return a comma separated list of short skill phrases.

Job:
{job_text}

Skills:
""")

def extract_job_skills(llm, job_text: str) -> str:
    prompt = JOB_PROMPT.format(job_text=job_text)
    result = llm(prompt)[0]["generated_text"]
    return result.strip()


#  CLEANING 

def clean_skill_list(text: str):
    text = text.replace("-", " ")
    raw_skills = re.split(r"[,\n]", text)

    skills = []

    for skill in raw_skills:
        s = skill.strip().lower()

        if len(s.split()) > 3:
            continue

        if not re.match(r"^[a-z0-9\s\+\#\.]+$", s):
            continue

        if len(s) > 2:
            skills.append(s)

    return list(set(skills))


#  FALLBACK 

def extract_job_skills_fallback(job_text: str):
    keywords = ["java", "llm", "english", "hungarian"]
    found = []

    for kw in keywords:
        if kw in job_text.lower():
            found.append(kw)

    return found