# Resume Analyzer

A Python-based tool that analyzes how well a resume matches a job description using text processing and cosine similarity.

## Overview

This project compares a resume against a job description and outputs a match percentage (0-100%). It uses **pandas** for data manipulation and **NumPy** for mathematical similarity calculations.

## How It Works

The analyzer follows a 5-step pipeline:

### 1. **File Reading**
Reads the resume and job description from text files.

### 2. **Text Cleaning**
- Converts all text to lowercase
- Removes punctuation and special characters
- Splits text into individual words

### 3. **Word Frequency Counting**
Uses pandas to count how many times each word appears in each document.

**Example:**
```
Resume words: ["python", "data", "python", "sql"]
Frequency: python=2, data=1, sql=1
```

### 4. **Data Alignment**
Combines both frequency counts into a single table where every unique word has a count from both documents.

**Example:**
```
           resume  job
python        2     1
data          1     2
java          1     0  ← only in resume
pandas        0     1  ← only in job
```

Missing values are filled with 0.

### 5. **Cosine Similarity Calculation**
Treats each document as a vector and computes the angle between them using NumPy.

**Formula:**
```
similarity = (A · B) / (||A|| × ||B||)
```

- **A · B** = dot product (measures overlap)
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
   Resume Analyzer v0.1

   ✓ Resume loaded: 187 characters
   ✓ Job description loaded: 215 characters

   ✓ Resume words: ['john', 'doe', 'software', ...]
   ✓ Job words: ['software', 'engineer', 'position', ...]

   📊 Top resume words:
   data        2
   python      1
   java        1
   ...

   📊 Aligned word frequencies:
              resume  job
   data         2.0  2.0
   python       1.0  1.0
   ...

   🎯 Match Score: 55.56%
   ❌ Bad match
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

- **80-100%:** Excellent match (rare unless resume is highly tailored)
- **60-79%:** Good match (worth applying)
- **50-59%:** Moderate match (consider tailoring resume)
- **0-49%:** Weak match (significant gaps)

**Note:** The current version (v1.0) treats all words equally, including names and common words. This can lower the match percentage. Future versions will filter out irrelevant words.

## Technologies Used

- **Python 3.x** - Core language
- **pandas** - Data manipulation and frequency counting
- **NumPy** - Mathematical similarity calculations
- **Regular expressions (re)** - Text cleaning

## Current Limitations (v0.01)

- Treats all words equally (names like "John" have same weight as skills like "Python")
- No stopword filtering (common words like "the", "a", "is" affect the score)
- No keyword weighting (technical skills aren't prioritized)
- Only supports plain text files

## Future Improvements (Planned)

- [ ] Stopword filtering (remove common words)
- [ ] Name detection and removal
- [ ] Keyword weighting (prioritize technical skills)
- [ ] Support for PDF files
- [ ] Web interface for file uploads
- [ ] Visualization of matching vs. non-matching words

## Learning Outcomes

This project demonstrates:
- File I/O in Python
- Text processing with regular expressions
- Data manipulation with pandas (Series, DataFrames, concat, fillna)
- Vector mathematics with NumPy (dot product, norms)
- Cosine similarity for text comparison
- Git version control and project structure

## License

This project is open source and available for educational purposes.

## Rifah Jesian

Built as a learning project to understand pandas, NumPy, and text analysis through practical application.