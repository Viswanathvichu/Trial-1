import moviepy.editor as mp

def merge_audio_video(video_file="video.mp4", audio_file="narration.wav", output="final_movie.mp4"):
    try:
        video = mp.VideoFileClip(video_file)
        audio = mp.AudioFileClip(audio_file)
        
        final_video = video.set_audio(audio)
        final_video.write_videofile(output, codec="libx264", fps=24)
        print(f"✅ Final movie saved as {output}")
    except Exception as e:
        print(f"Error during audio-video merging: {e}")


if __name__ == "__main__":
    merge_audio_video()
