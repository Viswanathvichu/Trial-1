import extract_text
import summarize_text
import generate_voice
import generate_images
import create_video
import merge_audio_video

if __name__ == "__main__":
    print("🚀 Starting AI Book to Movie Conversion...")
    extract_text.extract_text_from_pdf("book.pdf")
    summarize_text.summarize_text("extracted_text.txt")
    generate_voice.text_to_speech("summary.txt")
    generate_images.generate_images("summary.txt")
    create_video.create_video()
    merge_audio_video.merge_audio_video()
    print("🎬 Movie creation complete! Check 'final_movie.mp4' 🎉")
