from PIL import Image, ImageDraw, ImageFont
import os

def create_dummy_image(filename, size=(300, 200), color=(255, 0, 0), text="Test Post"):
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    draw.text((10, 90), text, font=font, fill=(255, 255, 255))
    save_path = os.path.join(r"C:\Users\Purvarajsinh\Desktop\blog_project\media\posts", filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    img.save(save_path, "JPEG")

images = [
    {"filename": "post1.jpg", "color": (0, 0, 255), "text": "Tech Gadgets"},
    {"filename": "post2.jpg", "color": (255, 255, 255), "text": "Laptop Screen"},
    {"filename": "post3.jpg", "color": (255, 165, 0), "text": "Vegan Dish"},
    {"filename": "post4.jpg", "color": (255, 0, 255), "text": "Homemade Pizza"},
    {"filename": "post5.jpg", "color": (0, 255, 0), "text": "Asian Temple"},
    {"filename": "post6.jpg", "color": (0, 128, 0), "text": "Airport Suitcase"},
    {"filename": "post7.jpg", "color": (255, 69, 0), "text": "Workout Scene"},
    {"filename": "post8.jpg", "color": (0, 0, 128), "text": "Meditation"},
    {"filename": "post9.jpg", "color": (139, 69, 19), "text": "Winter Outfit"},
    {"filename": "post10.jpg", "color": (128, 128, 128), "text": "Timeless Wardrobe"},
    {"filename": "post11.jpg", "color": (0, 255, 255), "text": "Smartwatch"},
    {"filename": "post12.jpg", "color": (75, 0, 130), "text": "Wireless Earbuds"},
    {"filename": "post13.jpg", "color": (255, 192, 203), "text": "Wall Art"},
    {"filename": "post14.jpg", "color": (255, 255, 224), "text": "Clutter-Free Kitchen"},
    {"filename": "post15.jpg", "color": (34, 139, 34), "text": "National Park"},
    {"filename": "post16.jpg", "color": (255, 140, 0), "text": "Hiking Gear"},
    {"filename": "post17.jpg", "color": (135, 206, 250), "text": "Morning Routine"},
    {"filename": "post18.jpg", "color": (0, 128, 128), "text": "Stress Relief"},
    {"filename": "post19.jpg", "color": (255, 99, 71), "text": "Street Food"},
    {"filename": "post20.jpg", "color": (210, 180, 140), "text": "Cozy Books"},
]

for img in images:
    create_dummy_image(
        filename=img["filename"],
        color=img["color"],
        text=img["text"]
    )
    print(f"Created image: {img['filename']}")