import re
print("Resume Analyzer v0.01")

def read_file(path):
    with open(path, "r") as f:
        return f.read()

resume_text = read_file("data/resume.txt")
job_description_text = read_file("data/job_description.txt")

print("\n Resume Loaded:", len(resume_text), "characters")
print("\n Job Description:", len(job_description_text), "characters")


def clean_text(text):
    """
    Converts text to lowercase, removes punctuation, and splits into a list of words.
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.split()

resume_words = clean_text(resume_text)
job_words = clean_text(job_description_text)

print("\n Resume Words:", resume_words[:10])
print("\n Job Words:", job_words[:10])


