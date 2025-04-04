import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text


if __name__ == "__main__":
    pdf_path = "book.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    
    if extracted_text:

    
        with open("extracted_text.txt", "w", encoding="utf-8") as f:
            f.write(extracted_text)
        print("✅ Text extraction complete! Saved to extracted_text.txt")
    else:
        print("❌ No text extracted.")
