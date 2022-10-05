#!/usr/bin/python3
import argparse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sqlite3


def add_text():
    img = Image.open(image_name)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("sans-serif.ttf", 16)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0),"Sample Text",(255,255,255),font=font)
    img.save('sample-out.jpg')

def main():
    parser = argparse.ArgumentParser(description='Document cool band names.')
    parser.add_argument('--band', type=str, nargs='+', help='a COOL band name')

    args = parser.parse_args()

    if args.band:
        if type(args.band) == list:
            band = " ".join(args.band)
        else:
            band = args.band
        # make art
        generate_band_art(band)

if __name__ == '__main__':
    main()



