import os
from PIL import Image, ImageDraw, ImageFont

import glob

for ic in range(3):
    frames = []
    imgs = glob.glob(f"iter_*_ic{ic}.png")
    for i in imgs:
        new_frame = Image.open(i)
        draw = ImageDraw.Draw(new_frame)
        filename = os.path.basename(i)

        # Define the text and position
        x = 10
        y = 10
        # Draw the text on the image
        draw.text((x, y), filename)
        frames.append(new_frame)

    frames[0].save(f'ic{ic}.gif', format='GIF', append_images=frames[1:],
                   save_all=True,
                   duration=600,
                   loop=1)
