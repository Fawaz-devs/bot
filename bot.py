import os
import random
from PIL import Image, ImageDraw, ImageFont

# Directory to save content
SAVE_DIR = "generated_content"
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

# Sample news headlines and articles
NEWS_HEADLINES = [
    "AI Takes Over Mundane Tasks, Freeing Humans for Creativity",
    "New Breakthrough in Quantum Computing Shocks Scientists",
    "Self-Driving Cars Expected to Reduce Traffic Accidents by 50%",
    "Tech Giants Invest Billions in Renewable Energy Solutions"
]

NEWS_ARTICLES = [
    "Artificial Intelligence is being increasingly used to automate repetitive tasks, allowing humans to focus on more creative and strategic work. Experts believe this shift will redefine multiple industries.",
    "Quantum computing has made a huge leap with a new breakthrough that promises faster computations than ever before. Researchers believe this will revolutionize fields such as cryptography and complex simulations.",
    "Self-driving cars are expected to reduce traffic-related fatalities by 50% over the next decade. Engineers are working on refining autonomous vehicle software to ensure safety and reliability.",
    "Big tech companies are pouring billions into renewable energy projects. Solar and wind power are now at the forefront of sustainable energy solutions, promising a greener future."
]

# Sample quotes
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs"
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

def generate_news():
    """Generates a random news article and saves it as a text file"""
    headline = random.choice(NEWS_HEADLINES)
    article = random.choice(NEWS_ARTICLES)
    news_path = os.path.join(SAVE_DIR, f"news_{random.randint(1000, 9999)}.txt")
    with open(news_path, "w") as file:
        file.write(f"Headline: {headline}\n\n{article}")
    print(f"News article saved: {news_path}")

def generate_quote():
    """Generates a random inspirational quote and saves it as a text file"""
    quote = random.choice(QUOTES)
    quote_path = os.path.join(SAVE_DIR, f"quote_{random.randint(1000, 9999)}.txt")
    with open(quote_path, "w") as file:
        file.write(quote)
    print(f"Quote saved: {quote_path}")

def generate_content(count=100):
    """Automatically generates 100 posts with mixed content"""
    for _ in range(count):
        choice = random.choice(["meme", "news", "quote"])
        if choice == "meme":
            generate_meme()
        elif choice == "news":
            generate_news()
        elif choice == "quote":
            generate_quote()

if __name__ == "__main__":
    generate_content(100)
