import re

def normalize_skill(skill: str) -> str:
    skill = skill.lower()
    skill = re.sub(r"\(.*?\)", "", skill)

    if skill.endswith("s"):
        skill = skill[:-1]

    return skill.strip()


def compute_match_score(cv_skills, job_skills):
    if not job_skills:
        return 0

    cv_norm = [normalize_skill(s) for s in cv_skills]
    job_norm = [normalize_skill(s) for s in job_skills]

    matches = [s for s in job_norm if s in cv_norm]

    return len(matches) / len(job_norm)