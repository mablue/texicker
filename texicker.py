from PIL import Image, ImageDraw, ImageFont
import textwrap
import re


# /////////////////////////
FONT1_SIZE = 150
FONT2_SIZE = 50

# ////////////////////////

# get data
quotes = ''
with open('files/data.ini', 'r') as file:
    quotes = file.read().replace('\n', '')
quotes = quotes.replace('     ', ' ').replace('     ', ' ').replace(
    '    ', ' ').replace('   ', ' ').replace('  ', ' ').replace('**', '\n').split('*')


# Open an Image

# Custom font style and font size
font1 = ImageFont.truetype('files/IranNastaliq.ttf', 120)
font2 = ImageFont.truetype('files/IranNastaliq.ttf', 50)

for quote in quotes[1:]:
    quote = quote.split("\n")
    quote[0] = textwrap.fill(quote[0],25)
    quote[1] = textwrap.fill(quote[1],70)

    img = Image.open('files/BG.jpg')




    # get a drawing context
    d1 = ImageDraw.Draw(img)
    d2 = ImageDraw.Draw(img)

    # draw multiline text
    d1.multiline_text((500, 50), quote[0], fill=(251, 242, 207), font=font1,anchor='ma',spacing=1,align="right")
    d2.multiline_text((10, 900), quote[1], fill=(250, 112, 112), font=font2,anchor='ls',spacing=1,align="left")

    quote = quote[1]+" "+quote[0]
    quote = " ".join(re.findall('[\u0622-\u06CC]+', quote))
    print(quote)


    try:
        img.save(f'stickers/{quote}.jpg')
    except:
        img.save(f'stickers/{quote[:130]}.jpg')

    del d1, d2,img


