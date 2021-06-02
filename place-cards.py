import csv
from PIL import Image, ImageDraw, ImageFont
import math
# image = Image.open('card-set.png')
# draw = ImageDraw.Draw(image)

font = ImageFont.truetype('AlexBrush-Regular.ttf', size=234)

# 382 high, 612 wide
w = 3096
h = 4008 / 2

def put_text(row, col, toptext, bottomtext, dr, toxoff=296, toyoff=308, drawRect=False):
    (tx, ty) = (row*w + toxoff, col*h + toyoff)
    # totext = "Jon Gao"
    color = 'rgb(0, 0, 0)' # black color
    
    (fx, fy) = (row*w + 95, col*h + 335)
    # fromtext = "Jon Gao"
    color = 'rgb(0, 0, 0)' # black color

    dr.text((tx, ty), toptext, fill=color, font=font)
    dr.text((fx, fy), bottomtext, fill=color, font=font)

with open('prom-tables.csv') as file:
    data = csv.reader(file)
    headers = next(data, None)
    print(headers)

    # if False:
    i=0
    data_list = list(data)
    num_rows = len(data_list)

    print(num_rows)
    
    while i < num_rows:
        row = data_list[i]
        try:
            row2 = data_list[i+1]
        except:
            row2 = ["",""]
        pageindex = math.floor(i / 2)

        if (pageindex == 0):
            image = Image.open('place-card.png')
            draw = ImageDraw.Draw(image)

        image = Image.open('place-card.png')
        draw = ImageDraw.Draw(image)

        name1 = row[1]
        name2 = row2[1]

        w1,h1 = font.getsize(name1)
        w2,h2 = font.getsize(name2)

        print(w1,h1)

        # draw.text((682,509), name1, fill='rgb(0,0,0)', font=font)
        draw.text((1548 - w1/2,1603 - h1/2), name1, fill='rgb(0,0,0)', font=font)

        # draw.text((682,2513), name2, fill='rgb(0,0,0)', font=font)
        draw.text((1548 - w2/2,3606 - h2/2), name2, fill='rgb(0,0,0)', font=font)

        image.save('./place-cards/'+str(pageindex)+'.png')
        
        i += 2

    # krouse = data        
        
        # put_text(pageindex % 2, (pageindex - (pageindex % 2)) / 2, row[0]+",", "", draw, toxoff=24, toyoff=224, drawRect=True)

        # image.save('./krouse/'+str(printindex//8)+'.png')
        # printindex += 1