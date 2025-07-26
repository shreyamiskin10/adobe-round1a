## 📄 ROUND 1A – Understand Your Document

### 🔍 Problem Statement
Given:
- A PDF file (up to 50 pages)

Your solution should:
- Extract the document title
- Extract all H1, H2, H3 headings
- Return a structured outline in JSON format with:
  - Heading level (H1/H2/H3)
  - Text
  - Page number

---

### 🧠 Approach

**1. PDF Parsing**
- Used `PyMuPDF (fitz)` to parse the PDF page by page.
- Extracted each text block with font size, position, and style metadata.

**2. Title Detection**
- First large, centered text from the first page is assumed to be the Title.

**3. Heading Detection**
- Grouped text blocks using font size and position.
- Font sizes are dynamically clustered into heading levels: H1 > H2 > H3.
- Also checked boldness and indentation for better accuracy.

**4. Heuristic Filters**
- Ignored:
  - Paragraphs or running text (based on font size, line length)
  - Captions or footnotes

**5. Output**
- JSON with `title` and `outline` array containing:
  - Level (H1, H2, H3)
  - Text content
  - Page number

---

<<<<<<< HEAD
### 📂 Directory Structure  
```
📦project-root/
 ┣ 📁input/               ← Placed input PDFs here (mounted inside container)
 ┣ 📁output/              ← Output JSONs saved here
 ┣ 📜setup.py   ← Main PDF parsing & outline logic
 ┣ 📜Dockerfile           ← Container definition
 ┣ 📜README.md            ← You're here!
```
=======
### 🧪 Example Output
>>>>>>> ca19b83 (Add Round 1B folder and combined README.md for Round 1A and 1B)

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

### ⚙️ Tech Stack
- Python 3.9
- PyMuPDF (fitz) – layout & font analysis
- pdfminer.six – optional fine-grained analysis
- json, re, os – utilities for parsing & output

---

### 🐳 Docker Instructions

**Build Image:**
```bash
docker build --platform linux/amd64 -t outline_extractor:uniqueid .
```

**Run Container:**
```bash
docker run --rm   -v $(pwd)/input:/app/input   -v $(pwd)/output:/app/output   --network none   outline_extractor:uniqueid
```

---

### 📁 Project Structure

```
project-root/
 ┣ 📁input/       ← Input PDFs
 ┣ 📁output/      ← Output JSONs
 ┣ 📜setup.py     ← Core logic (PDF to JSON)
 ┣ 📜Dockerfile   ← Docker setup
 ┣ 📜README.md    ← Docs
```

---

### ✅ Key Features

- 🧠 Smart Title & Heading Extraction
- 📦 JSON Output with hierarchy and page references
- 🌐 Multilingual Support (UTF-8)
- 🐳 Fully Offline & Dockerized
- ⚡ Fast Processing (<10s for 50-page PDFs)
- 💾 Lightweight (<200MB, CPU-only)

---

### 🔁 Reusability
- Modular functions
- No hardcoded rules
- Optimized for future rounds (e.g., semantic search in Round 1B)