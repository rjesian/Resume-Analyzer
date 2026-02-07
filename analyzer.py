import re
import pandas as pd
import numpy as np

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

# Converting word lists to panda Series
resume_series = pd.Series(resume_words)
job_series = pd.Series(job_words)

# Count word frequencies
resume_freq = resume_series.value_counts()
job_freq = job_series.value_counts()

print("\nTop Resume Words:")
print(resume_freq.head())
print("\nTop Job Description Words:")
print(job_freq.head())

df = pd.concat([resume_freq, job_freq], axis=1, keys=["resume", "job"])
df = df.fillna(0)

print("\n Aligned Word Frequencies:")
print(df.head(10))

# Extract vectors from DataFrame
resume_vector = df["resume"].to_numpy()
job_vector = df["job"].to_numpy()

# Compute cosine similarity
dot_product = np.dot(resume_vector, job_vector)
resume_norm = np.linalg.norm(resume_vector)
job_norm = np.linalg.norm(job_vector)

similarity = dot_product / (job_norm * resume_norm)

match_percentage = round(similarity * 100, 2)
print(f"\n Resume Match Percentage: {match_percentage}%")

if match_percentage >= 60:
    print("\n Good match")
else:
    print("\n Bad match")




