import csv
from PIL import Image, ImageDraw, ImageFont

# image = Image.open('card-set.png')
# draw = ImageDraw.Draw(image)

font = ImageFont.truetype('GRIFTER.otf', size=23)

# 382 high, 612 wide
w = 612
h = 382

def put_text(row, col, totext, fromtext, dr, toxoff=296, toyoff=308, drawRect=False):
    (tx, ty) = (row*w + toxoff, col*h + toyoff)
    # totext = "Jon Gao"
    color = 'rgb(0, 0, 0)' # black color
    
    (fx, fy) = (row*w + 95, col*h + 335)
    # fromtext = "Jon Gao"
    color = 'rgb(0, 0, 0)' # black color

    if drawRect:
        draw.rectangle([(18 + row*w,224 + col*h),(30 + row*w,238 + col*h)], fill='rgb(255,255,255)')

    dr.text((tx, ty), totext, fill=color, font=font)
    dr.text((fx, fy), fromtext, fill=color, font=font)

krouse = []

with open('data-final.csv') as file:
    data = csv.reader(file)
    headers = next(data, None)
    print(headers)
    printindex = 0
    # if False:
    for row in data:
        if row[2] == "Dr. Krouse":
            krouse.append(row)
            continue
        pageindex = printindex % 8
        if (pageindex == 0):
            image = Image.open('card-set.png')
            draw = ImageDraw.Draw(image)
        
        put_text(pageindex % 2, (pageindex - (pageindex % 2)) / 2, row[0], row[2], draw)

        image.save('./final/'+str(printindex//8)+'.png')
        printindex += 1

    # krouse = data

    print(krouse)
    printindex = 0
    for row in krouse:
        pageindex = printindex % 8
        if (pageindex == 0):
            image = Image.open('card-krouse-set.png')
            draw = ImageDraw.Draw(image)
        
        
        put_text(pageindex % 2, (pageindex - (pageindex % 2)) / 2, row[0]+",", "", draw, toxoff=24, toyoff=224, drawRect=True)

        image.save('./krouse/'+str(printindex//8)+'.png')
        printindex += 1