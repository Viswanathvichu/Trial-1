import moviepy.editor as mp
import os

def create_video(output_video="video.mp4", duration_per_image=5):
    images = sorted([img for img in os.listdir() if img.endswith(".png")])  # Ensure they are in order

    images.sort()  # Ensure they are in order

    try:
        clips = [mp.ImageClip(img).set_duration(duration_per_image) for img in images]
        video = mp.concatenate_videoclips(clips, method="compose")
        video.write_videofile(output_video, fps=24)
        print(f"✅ Video saved as {output_video}")
    except Exception as e:
        print(f"Error during video creation: {e}")


if __name__ == "__main__":
    create_video()
