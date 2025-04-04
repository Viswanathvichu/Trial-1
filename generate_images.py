import torch
from diffusers import StableDiffusionPipeline

def generate_images(text, num_images=5):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    for i in range(num_images):
        try:
            image = pipe(text, num_inference_steps=30).images[0] 
            image.save(f"image_{i+1}.png")
            print(f"✅ Image {i+1} saved as image_{i+1}.png")
        except Exception as e:
            print(f"Error generating image {i+1}: {e}")


if __name__ == "__main__":
    with open("extracted_text.txt", "r", encoding="utf-8") as f:
        text = f.read()


    generate_images(text)
