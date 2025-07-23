import fitz  # PyMuPDF

def extract_outline(pdf_path):
    # Open the PDF using PyMuPDF
    doc = fitz.open(pdf_path)

    blocks = []  # This will store all text blocks with details

    # Loop through all pages of the document
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # Extract text in dictionary format (includes font size and position)
        for b in page.get_text("dict")["blocks"]:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        # Save necessary text span info
                        blocks.append({
                            "text": s["text"].strip(),
                            "size": s["size"],          # Font size
                            "font": s["font"],          # Font name
                            "bold": "Bold" in s["font"],# Is bold font
                            "page": page_num + 1,       # 1-indexed page number
                            "y": s["bbox"][1]           # Y-position (for top-of-page detection)
                        })

    # Remove empty text spans
    blocks = [b for b in blocks if b["text"]]

    # Sort font sizes in descending order to detect title and heading levels
    sizes = sorted(set([b["size"] for b in blocks]), reverse=True)

    # Map top font sizes to heading levels
    size_to_level = {}
    if sizes:
        size_to_level[sizes[0]] = "title"  # Largest font size = Title
    if len(sizes) > 1:
        size_to_level[sizes[1]] = "H1"
    if len(sizes) > 2:
        size_to_level[sizes[2]] = "H2"
    if len(sizes) > 3:
        size_to_level[sizes[3]] = "H3"

    # Try to extract document title using the largest font block
    title = next((b["text"] for b in blocks if size_to_level.get(b["size"]) == "title"), "Untitled")

    outline = []

    # Go through blocks and classify H1/H2/H3 based on size mapping
    for b in blocks:
        level = size_to_level.get(b["size"])

        # Filter only potential headings (based on logic below)
        if level in ["H1", "H2", "H3"] and is_potential_heading(b["text"]):
            outline.append({
                "level": level,
                "text": b["text"],
                "page": b["page"]
            })

    # If the document is a form (too many headings on page 1), ignore outline
    if len(outline) > 25 and all(h["page"] == 1 for h in outline):
        outline = []

    return {
        "title": title,
        "outline": outline
    }

def is_potential_heading(text):
    """
    Rule-based filter to determine if a text block is a real heading.
    Adjusted to avoid junk like "1.", "Rs.", etc.
    """
    if not text:
        return False
    if len(text) < 4:  # Too short
        return False
    if text.strip().isdigit():  # Only a number like "1." or "12."
        return False
    # if len(text.split()) > 25:  # Too long, likely a paragraph
    #     return False
    if len(text.strip()) <= 2:  # Single letter or abbreviation
        return False
    return True
