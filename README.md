# Adobe - Connecting the Dots Challenge (Round 1A)

## Overview

We are excited to be selected for the **"Connecting the Dots"** challenge by Adobe.  
Our current focus is **Round 1A**, which involves building an intelligent system to extract structured outlines from PDFs — identifying the **Title**, **H1**, **H2**, and **H3** headings with corresponding page numbers in a clean hierarchical JSON format.

## Problem Statement

Extract the structural hierarchy of a PDF document to enable smarter, contextual document understanding. This extracted outline forms the foundation for advanced downstream tasks like semantic search, summarization, and cross-reference mapping.

## Functional Requirements

- Accept a PDF file (≤ 50 pages)
- Extract:
  - `Title`
  - `Headings` (H1, H2, H3 with `level`, `text`, `page`)
- Output format (example):

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

## Our Approach

We are designing a robust PDF parser capable of analyzing text, layout, font hierarchy, and structural cues.

**Key pipeline features:**

- Offline-first operation
- Runtime within 10 seconds for 50-page PDFs
- Model/container ≤ 200MB and CPU-only execution (amd64)

## How to Build & Run

> **Note:** The container is designed to run automatically as per the organizer’s evaluation script.

- All PDFs placed in `/app/input` will be processed.
- Corresponding `.json` outputs will be generated in `/app/output`.

## Tech Stack

- Python (core logic)
- PDF parsing libraries (e.g., PyPDF2, pdfminer, etc.)
- Docker for containerization

## Status

- ✅ Repository initialized
- 🛠️ Outline extractor in development
- 📄 Current task: Title & heading structure extraction logic

---

Stay tuned for further updates as we progress towards Round 1B.
