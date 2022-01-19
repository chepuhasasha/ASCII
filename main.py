from PIL import Image
imag = Image.open("1.png")
imag = imag.convert('RGB')

width = 100
height = 40
resized_img = imag.resize((width, height), Image.ANTIALIAS)


def brightness(x, y):
    pixelRGB = resized_img.getpixel((x, y))
    R, G, B = pixelRGB
    return round(sum([R, G, B])/3)


def symbol(brightness):
    return {
        brightness < 50: ' ',
        50 <= brightness < 100: '7',
        100 <= brightness < 150: '2',
        150 <= brightness < 200: '1',
        200 <= brightness < 255: '5',
        255 <= brightness: '8'
        # brightness < 50: '  ',
        # 50 <= brightness < 100: '░░',
        # 100 <= brightness < 150: '▒▒',
        # 150 <= brightness < 200: '▓▓',
        # 200 <= brightness < 255: '▓▓',
        # 255 <= brightness: '██'
    }[True]


h = 1
result = []
while h < height:
    w = 1
    line = ''
    while w < width:
        s = symbol(brightness(w, h))
        line += s
        w += 1
    result.append(line)
    h += 1

with open('data.txt', "wb") as file:
    for line in result:
        file.write(str(line + '\n').encode("UTF-8"))


for line in result:
    print(line)
