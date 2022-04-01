from PIL import Image, ImageDraw, ImageFont

image = Image.open('blank.jpg')
width, height = image.size
draw = ImageDraw.Draw(image)

def writeName(name):
    text = name
    textwidth, textheight = draw.textsize(text)
    WidthMargin = width / 2 + 250
    HeightMargin = height / 2 - 20
    x = width - textwidth - WidthMargin
    y = height - textheight - HeightMargin
    font = ImageFont.truetype("Helvetica.ttf", 120)
    draw.text((x, y), text, font=font, fill="#FF0000")

def writePersonalMessage(personal):
    text = personal
    textwidth, textheight = draw.textsize(text)
    WidthMargin = width / 2 + 450
    HeightMargin = height / 2 - 600
    x = width - textwidth - WidthMargin
    y = height - textheight - HeightMargin
    font = ImageFont.truetype("Helvetica.ttf", 120)
    draw.text((x, y), text, font=font, fill="#FF0000")


def getImage(name, personal):
    global image
    global width
    global height
    global draw
    image = Image.open('blank.jpg')
    width, height = image.size
    draw = ImageDraw.Draw(image)
    writeName(name)
    writePersonalMessage(personal)
    return image


