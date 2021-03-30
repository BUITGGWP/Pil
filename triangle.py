from math import sqrt
import line
from PIL import Image, ImageDraw
import functions as f


def triangle(x1, y1, length):
    x2 = round(x1 + length / 2)
    x3 = round(x1 + length)
    heigth = sqrt(pow(length, 2) - pow((length / 2), 2))
    y2 = round(y1 - heigth)
    y3 = y1
    line(x1, y1, x2, y2)
    line(x2, y2, x3, y3)
    line(x3, y3, x1, y1)


def line(x1, y1, x, y):
    deltax = f.abs(x - x1)
    deltay = f.abs(y - y1)
    length = f.max(deltax, deltay)
    if length == 0:
        draw.point((x1, y1), fill=(0, 0, 0))
        return 0
    dx = (x - x1) / length
    dy = (y - y1) / length
    x2 = x1
    y2 = y1
    while length != 0:
        draw.point((round(x2), round(y2)), fill=(0, 0, 0))
        x2 += dx
        y2 += dy
        length -= 1


new_image = Image.new("RGB", (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(new_image)
triangle(20, 250, 236)
new_image.save("124.png", "PNG")