from transformers import pipeline

def summarize_text(text, max_length=200):
    try:
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error during summarization: {e}")
        return ""


if __name__ == "__main__":
    with open("extracted_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    summary = summarize_text(text)
    
    if summary:

    
        with open("summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)
        print("✅ Summarization complete! Saved to summary.txt")
    else:
        print("❌ No summary generated.")
