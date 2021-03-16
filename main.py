from PIL import Image, ImageDraw


def line_vert(x, y, l):
    new_image = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    if l < 0:
        for i in range(l * -1):
            draw.point((y, x - 1), fill=(0, 0, 0))
            x = x - 1
    else:
        for i in range(l * 1):
            print(x, y)
            draw.point((y, x + 1), fill=(0, 0, 0))
            x = x + 1
    return new_image.save('test.png', 'PNG')


def line_goriz(x, y, l):
    new_image = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    if l < 0:
        for i in range(l * -1):
            draw.point((x - 1, y), fill=(0, 0, 0))
            x = x - 1
    else:
        for i in range(l * 1):
            #print(x, y)
            draw.point((x + 1, y), fill=(0, 0, 0))
            x = x + 1
    return new_image.save('test.png', 'PNG')

line_goriz(200, 200, -100)