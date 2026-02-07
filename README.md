# Resume Analyzer

A Python-based tool that analyzes how well a resume matches a job description using text processing, stopword filtering, and cosine similarity.

## Overview

This project compares a resume against a job description and outputs a match percentage (0-100%). It uses **pandas** for data manipulation, **NumPy** for mathematical similarity calculations, and implements **stopword filtering** to focus on relevant keywords.

## How It Works

The analyzer follows a 6-step pipeline:

### 1. **File Reading**
Reads the resume and job description from plain text files.

### 2. **Text Cleaning**
- Converts all text to lowercase
- Removes punctuation and special characters using regex
- Splits text into individual words

**Example:**
```
Input:  "Skills: Python, Java, SQL!"
Output: ["skills", "python", "java", "sql"]
```

### 3. **Stopword Filtering**
Removes common words that don't contribute to job matching:
- Articles: the, a, an
- Conjunctions: and, or, but
- Prepositions: in, on, at, to, from
- Pronouns: I, you, he, she, it
- Common verbs: is, are, was, have, do

**Why this matters:** Focuses comparison on actual keywords (like "python", "sql") rather than generic language.

### 4. **Word Frequency Counting**
Uses pandas to count how many times each word appears in each document.

**Example:**
```
Resume words: ["python", "data", "python", "sql"]
Frequency: python=2, data=1, sql=1
```

### 5. **Data Alignment**
Combines both frequency counts into a single DataFrame where every unique word has a count from both documents.

**Example:**
```
           resume  job
python        2     1
data          1     2
java          1     0  ← only in resume
pandas        0     1  ← only in job
```

Missing values are filled with 0.

### 6. **Cosine Similarity Calculation**
Treats each document as a vector and computes the angle between them using NumPy.

**Formula:**
```
similarity = (A · B) / (||A|| × ||B||)
```

- **A · B** = dot product (measures overlap between vectors)
- **||A||, ||B||** = vector magnitudes (normalization)

The result is a number between 0 (no match) and 1 (perfect match), converted to a percentage.

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository:**
```bash
   git clone https://github.com/YOUR-USERNAME/resume-analyzer.git
   cd resume-analyzer
```

2. **Create a virtual environment:**
```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

## Usage

1. **Add your resume and job description:**
   - Place your resume text in `data/resume.txt`
   - Place the job description in `data/job_description.txt`

2. **Run the analyzer:**
```bash
   python analyzer.py
```

3. **View the results:**
```
   Resume Analyzer v0.01

   Resume Loaded: 194 characters
   Job Description: 210 characters

   Resume Words: ['software', 'engineer', 'skills', 'python', 'java', ...]
   Job Words: ['software', 'engineer', 'position', 'required', 'skills', ...]

   Top Resume Words:
   data        2
   software    1
   engineer    1
   python      1
   java        1

   Top Job Description Words:
   data        2
   software    1
   engineer    1
   position    1
   required    1

   Aligned Word Frequencies:
              resume  job
   data         2.0  2.0
   software     1.0  1.0
   engineer     1.0  1.0
   skills       1.0  1.0
   python       1.0  1.0

   Resume Match Percentage: 58.83%

   Good match
```

## Project Structure
```
resume-analyzer/
├── .gitignore           # Ignores .venv, IDE files, etc.
├── requirements.txt     # Python dependencies (pandas, numpy)
├── analyzer.py          # Main analysis script
├── data/
│   ├── resume.txt       # Your resume (plain text)
│   └── job_description.txt  # Job description (plain text)
└── README.md            # This file
```

## Understanding the Match Percentage

- **70-100%:** Strong match (resume aligns well with job requirements)
- **50-69%:** Moderate match (some alignment, may need tailoring)
- **0-49%:** Weak match (significant gaps in requirements)

**Threshold:** Currently set at 50% for a "good match"

## Technologies Used

- **Python 3.x** - Core language
- **pandas** - Data manipulation, Series, DataFrames, value counting, alignment
- **NumPy** - Vector operations, dot product, norm calculations
- **Regular expressions (re)** - Text cleaning and pattern matching

## Current Limitations (v2.0)

### 1. **Manual Stopword List**
- Stopwords are hardcoded (includes common English words + names)
- Doesn't automatically identify domain-specific filler words
- Requires manual updates for different contexts

### 2. **Equal Word Weighting**
- All non-stopwords are treated equally
- "Python" (technical skill) has same weight as "experience" (generic term)
- Doesn't prioritize job-critical keywords

### 3. **No Semantic Understanding**
- "machine learning" and "ML" are treated as different
- Synonyms aren't recognized (e.g., "developed" vs "built")
- No understanding of skill relationships

### 4. **Text-Only Input**
- Only supports plain text files
- No PDF or Word document support
- No parsing of structured resume formats

### 5. **Single Document Comparison**
- Compares one resume to one job description at a time
- No batch processing or ranking multiple jobs

## Future Improvements (Planned)

- [ ] **TF-IDF weighting** - Automatically downweight common words without hardcoding
- [ ] **Keyword weighting** - Prioritize technical skills over generic terms
- [ ] **PDF support** - Parse PDF resumes and job descriptions
- [ ] **Synonym detection** - Recognize related terms (e.g., "ML" = "machine learning")
- [ ] **Skill extraction** - Use NLP to identify only relevant technical skills
- [ ] **Visualization** - Chart showing matching vs. non-matching keywords
- [ ] **Batch processing** - Compare one resume against multiple job descriptions
- [ ] **Web interface** - Upload files through a browser instead of command line

## Learning Outcomes

This project demonstrates:
- **File I/O** in Python
- **Text processing** with regular expressions
- **Data structures** - lists, sets, dictionaries
- **pandas fundamentals** - Series, DataFrames, concat, fillna, value_counts
- **NumPy operations** - arrays, dot product, vector norms
- **Cosine similarity** for text comparison
- **Stopword filtering** for text analysis
- **Git version control** and incremental development
- **Project structure** and documentation best practices

## Key Concepts Learned

### **Pandas:**
- Converting lists to Series with `pd.Series()`
- Counting frequencies with `.value_counts()`
- Combining data with `pd.concat()`
- Handling missing data with `.fillna()`
- Converting to NumPy arrays with `.to_numpy()`

### **NumPy:**
- Dot product calculation with `np.dot()`
- Vector magnitude with `np.linalg.norm()`
- Array operations for mathematical computations

### **Text Processing:**
- Regex patterns for text cleaning
- Stopword filtering techniques
- Frequency-based text analysis

## License

This project is open source and available for educational purposes.

## Rifah Jesian

Built as a learning project to understand pandas, NumPy, and text analysis through practical application.

---

## Version History

- **v0.02** - Added stopword filtering to improve accuracy
- **v0.01** - Initial implementation with basic text matching and cosine similarity