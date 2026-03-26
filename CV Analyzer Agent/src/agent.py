from src.parsing import extract_text_from_cv
from src.tools import (
    extract_skills_from_section,
    extract_job_skills,
    extract_job_skills_fallback,
    clean_skill_list,
)
from src.scoring import compute_match_score


def run_cv_agent(llm, cv_file_path: str, job_text: str):

    # 1. CV → text
    cv_text = extract_text_from_cv(cv_file_path)

    # 2. CV skills – deterministic
    cv_skills = extract_skills_from_section(cv_text)

    # 3. Job skills – LLM
    job_skills_raw = extract_job_skills(llm, job_text)
    job_skills = clean_skill_list(job_skills_raw)

    # 4. Fallback ha LLM üres
    if not job_skills:
        job_skills = extract_job_skills_fallback(job_text)

    # 5. Scoring
    score = compute_match_score(cv_skills, job_skills)

    return {
        "cv_skills": cv_skills,
        "job_skills": job_skills,
        "score": score,
        "raw_job_output": job_skills_raw,
    }