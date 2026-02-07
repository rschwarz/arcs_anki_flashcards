from functools import partial
from pathlib import Path

from PIL import Image, ImageFilter

# path where we all the image files are stored
root = Path("../cards/content/card-images/arcs/en-US")

# path where the processed images are stored
target = Path("imgs")
target.mkdir(exist_ok=True)

# list of cards, by type
guild_cards = [f"BC{i:02d}.png" for i in range(1, 25 + 1)]
vox_cards = [f"BC{i:02d}.png" for i in range(26, 31 + 1)]
lore_cards = [f"L{i:02d}.png" for i in range(1, 28 + 1)]
leader_cards = [f"LEAD{i:02d}.png" for i in range(1, 16 + 1)]

def resize_card(input_path: Path) -> None:
    img = Image.open(input_path)

    # shrink it by 50% in either dimension
    w, h = img.size
    img2 = img.resize((w//2, h//2), Image.LANCZOS)

    # store it in new position
    output_path = target / input_path.name
    img2.save(output_path, format="PNG")

def blur_card(input_path: Path, prop1, prop2):
    "Blur a vertical section of a card."
    img = Image.open(input_path)
    w, h = img.size

    left, top, right, bottom = (0, int(prop1 * h), w, int(prop2 * h))

    region = img.crop((left, top, right, bottom))
    blurred = region.filter(ImageFilter.GaussianBlur(5))
    img.paste(blurred, (left, top))

    output_path = target / ("blur_" + input_path.name)
    img.save(output_path, format="PNG")

blur_guild_card = partial(blur_card, prop1=0.65, prop2=0.9)
blur_vox_card = partial(blur_card, prop1=0.12, prop2=0.42)
blur_lore_card = blur_guild_card
blur_leader_card = partial(blur_card, prop1=0.59, prop2=0.87)

# actually do the processing
for gc in guild_cards:
    resize_card(root / gc)
    blur_guild_card(target / gc)
for vc in vox_cards:
    resize_card(root / vc)
    blur_vox_card(target / vc)
for lore in lore_cards:
    resize_card(root / lore)
    blur_lore_card(target / lore)
for leader in leader_cards:
    resize_card(root / leader)
    blur_leader_card(target / leader)
