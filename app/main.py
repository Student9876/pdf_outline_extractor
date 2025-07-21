# app/main.py

import os
import json
from extractor import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            filepath = os.path.join(INPUT_DIR, filename)
            outline = extract_outline(filepath)
            json_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(outline, f, indent=2)

if __name__ == "__main__":
    main()
