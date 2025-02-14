import os
import random
from PIL import Image, ImageDraw, ImageFont

# Directory to save memes
SAVE_DIR = "generated_memes"
os.makedirs(SAVE_DIR, exist_ok=True)

# Directory for background images
BG_DIR = "backgrounds"
os.makedirs(BG_DIR, exist_ok=True)

# Sample text for memes
MEME_TEXTS = [
    "When you realize it's Monday again...",
    "Me trying to act normal after 8 cups of coffee",
    "That moment when you forget why you walked into the room",
    "Coding at 2 AM be like...",
    "When AI does your work and you still get paid"
]

def get_random_background():
    """Selects a random image from the backgrounds folder"""
    images = [img for img in os.listdir(BG_DIR) if img.endswith((".png", ".jpg", ".jpeg"))]
    if not images:
        return Image.new("RGB", (500, 500), (255, 255, 255))  # Default white background if no images
    return Image.open(os.path.join(BG_DIR, random.choice(images))).resize((500, 500))

def generate_meme():
    """Generates a random meme image with text on a background"""
    img = get_random_background()
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    text = random.choice(MEME_TEXTS)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    position = ((500 - text_width) // 2, (500 - text_height) // 2)
    
    # Add text shadow for readability
    shadow_offset = 2
    draw.text((position[0] + shadow_offset, position[1] + shadow_offset), text, fill="black", font=font)
    draw.text(position, text, fill="white", font=font)
    
    meme_path = os.path.join(SAVE_DIR, f"meme_{random.randint(1000, 9999)}.png")
    img.save(meme_path)
    print(f"Meme saved: {meme_path}")

# Generate multiple memes
def generate_multiple_memes(count=5):
    for _ in range(count):
        generate_meme()

if __name__ == "__main__":
    generate_multiple_memes(3)