#!/usr/bin/env python3
import asyncio
import os

from PIL import Image, ImageDraw, ImageFont

from lib import epd4in2
from get_cluster_info import get_cluster_info, get_node_names

dir_path = os.path.dirname(os.path.realpath(__file__))

FONT_FILE = "Meslo-Regular.ttf"
FONT_SIZE = 16
FONT_STYLE = 5

print("Initializing screen...")
display = epd4in2.EPD()
display.init()
print("Clearing screen...")

WIDTH, HEIGHT = display.width, display.height

print("Loading fonts...")
font = ImageFont.truetype(os.path.join(os.path.join(dir_path, "fonts"), FONT_FILE), FONT_SIZE)

print("Generating image...")

image = Image.new(mode='1', size=(WIDTH, HEIGHT), color=255)


def progress_bar(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, progress: float):
    if progress > 1:
        progress = progress / 100
    draw.rectangle([x, y, x + w, y + h], outline=0)
    draw.rectangle([x, y, x + w * progress, y + h], fill=0)


def draw_info_box(draw: ImageDraw.ImageDraw, x: int, y: int, node_info: dict):
    W_BOX, H_BOX = WIDTH, HEIGHT / 4
    P_UP, P_LEFT = 2, 2
    Y_1, Y_2, Y_3 = y + P_UP, y + P_UP * 5 + font.size + 1, y + P_UP * 9 + font.size * 2
    X_1, X_2, X_3 = x + P_LEFT, x + P_LEFT + 120, x + P_LEFT + 256
    pretty_percent = lambda x: f"{x * 100:.2f}%".replace("0%", "%").replace(".0%", "%")
    draw.rectangle([x, y, x + W_BOX, y + H_BOX], outline=0)

    draw.text([X_1, Y_1], f"  {node_info['hostname']}", font=font)
    draw.text([X_1, Y_2], f"  {node_info['cpu_temp']['']:.2f}ºC", font=font)
    draw.text([X_1, Y_3], f"  {pretty_percent(node_info['disk_usage']['percent'] / 100)}", font=font)

    draw.text([X_2, Y_1], f" 0", font=font)
    progress_bar(draw, X_2 + 39, Y_1 + 5, 85, 10, node_info['cpu_usage'][0])
    draw.text([X_2, Y_2], f" 1", font=font)
    progress_bar(draw, X_2 + 39, Y_2 + 5, 85, 10, node_info['cpu_usage'][1])

    draw.text([X_3, Y_1], f" 2", font=font)
    progress_bar(draw, X_3 + 39, Y_1 + 5, 85, 10, node_info['cpu_usage'][2])
    draw.text([X_3, Y_2], f" 3", font=font)
    progress_bar(draw, X_3 + 39, Y_2 + 5, 85, 10, node_info['cpu_usage'][3])

    draw.text([X_2 - 40, Y_3], f"RAM", font=font)
    progress_bar(draw, X_2, Y_3 + 5, 260, 10, node_info['ram_usage']['percent'])


draw = ImageDraw.Draw(image)

nodes_information = asyncio.run(get_cluster_info(get_node_names()))

for i, node_info in enumerate(nodes_information):
    draw_info_box(draw, 0, int((HEIGHT / 4)) * i, node_info)

print("Transposing...")
image = image.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT)

print("Displaying in screen...")
display.display(display.getbuffer(image))
print("Done!")
