from PIL import Image, ImageDraw


def line_vert(x, y, l, new_image):
    #new_image = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    draw.point((x, y), fill=(0, 0, 0))
    if l < 0:
        for i in range(l * -1):
            draw.point((x - 1, y - 1), fill=(0, 0, 0))
            y = y - 1
    else:
        for i in range(l):
            #print(x, y)
            draw.point((x, y + 1), fill=(0, 0, 0))
            y = y + 1
    return new_image


def line_goriz(x, y, l, new_image):
    #new_image = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    if l < 0:
        for i in range(l * -1):
            draw.point((x - 1, y), fill=(0, 0, 0))
            x = x - 1
    else:
        for i in range(l):
            #print(x, y)
            draw.point((x, y), fill=(0, 0, 0))
            x = x + 1
    return new_image

def rectangle(x, y, w, h, new_image):
    #new_image = Image.new("RGB", (500, 500), (255, 255, 255))
    #draw = ImageDraw.Draw(new_image)
    xyw = [x + w, y]
    xyh = [x, y + h]
    print(x, y)
    draw = ImageDraw.Draw(new_image)
    draw.point((x, y), fill=(0, 0, 0))
    line_goriz(x, y, w, new_image)
    line_vert(x, y, h, new_image)
    line_goriz(xyh[0], xyh[1], w, new_image)
    line_vert(xyw[0], xyw[1], h, new_image)

def vert_dio(sp, new_image, w=50, h=50):
    w_v = w * len(sp) + 5 * len(sp)
    max_sp = max(sp)
    line_goriz(w + 20, max_sp * h + h, w_v * 3, new_image)
    for j, i in enumerate(sp):
        rectangle(w + 20, max_sp * h + h - (i * 10), 10, i * 10, new_image)
        w = 50
        w = w + ((j + 1) * 20)






new_image = Image.new("RGB", (1000, 1000), (255, 255, 255))
#line_vert(5, 50, 100, new_image)
#rectangle2(100, 100, 50, 50, new_image)
vert_dio([2, 5, 3, 7, 9 ,8 ,6], new_image)
new_image.save('test.png', 'PNG')