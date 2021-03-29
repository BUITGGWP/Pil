from PIL import Image, ImageDraw


def line_vert(x, y, l, new_image, color=(0, 0, 0)):
    #new_image = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    draw.point((x, y), fill=color)
    if l < 0:
        for i in range(l * -1):
            draw.point((x - 1, y - 1), fill=color)
            y = y - 1
    else:
        for i in range(l):
            #print(x, y)
            draw.point((x, y + 1), fill=color)
            y = y + 1
    return new_image


def line_goriz(x, y, l, new_image, color=(0, 0, 0)):
    #new_image = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    if l < 0:
        for i in range(l * -1):
            draw.point((x - 1, y), fill=color)
            x = x - 1
    else:
        for i in range(l):
            #print(x, y)
            draw.point((x, y), fill=color)
            x = x + 1
    return new_image

def rectangle(x, y, w, h, new_image, color=(0, 0, 0)):
    #new_image = Image.new("RGB", (500, 500), (255, 255, 255))
    #draw = ImageDraw.Draw(new_image)
    xyw = [x + w, y]
    xyh = [x, y + h]
    print(x, y)
    draw = ImageDraw.Draw(new_image)
    draw.point((x, y), fill=color)
    line_goriz(x, y, w, new_image, color)
    line_vert(x, y, h, new_image, color)
    line_goriz(xyh[0], xyh[1], w, new_image, color)
    line_vert(xyw[0], xyw[1], h, new_image, color)

def vert_dio(sp, new_image, color=(0, 0, 0), w=50, h=50):
    w_v = w * len(sp) + 5 * len(sp)
    max_sp = max(sp)
    line_goriz(w + 20, max_sp * h + h, w_v * 3, new_image, color)
    for j, i in enumerate(sp):
        rectangle(w + 20, max_sp * h + h - (i * 10), 10, i * 10, new_image, color)
        w = 50
        w = w + ((j + 1) * 20)



def draw_line(x1, y1, x2, y2, new_image, color=(0, 0, 0)):
    deltay = abs(y1 - y2)
    deltax = abs(x1 - x2)
    draw = ImageDraw.Draw(new_image)
    lenght = max([deltax, deltay])
    if y1 < y2:
        deltay = abs(y2 - y1)
    if x1 < x2:
        deltax = abs(x2 - x1)
    dx = deltax / lenght
    dy = deltay / lenght
    x = x1
    y = y1
    while lenght != 0:
        draw.point((round(x), round(y)), color)
        x += dx
        y += dy
        lenght -= 1


def draw_square(x1, y1, lenht, new_image, color=(0, 0, 0)):
    rectangle(x1, y1, lenht, lenht, new_image, color)



new_image = Image.new("RGB", (500, 500), (255, 255, 255))
#line_vert(5, 50, 100, new_image)
#rectangle2(100, 100, 50, 50, new_image)
#vert_dio([2, 5, 3, 7, 9 ,8 ,6], new_image)
draw_square(100, 100, 10, new_image)
new_image.save('test.png', 'PNG')
