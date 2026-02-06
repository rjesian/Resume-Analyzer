print("Resume Analyzer v0.01")

def read_file(path):
    with open(path, "r") as f:
        return f.read()

resume_text = read_file("data/resume.txt")
job_description_text = read_file("data/job_description.txt")

print("\n Resume Loaded:", len(resume_text), "characters")
print("\n Job Description:", len(job_description_text), "characters")


