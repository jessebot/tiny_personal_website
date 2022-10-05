#!/usr/bin/env python3
# script by jessebot@linux.com to get the bands' art and do the things
# 1/10/19 -- 2019? D:
import argparse
import datetime
from google_images_download import google_images_download
import sqlite3


def generate_band_art(band):
    # change image results by making different key words
    band_list = band.split()
    last_item = len(band_list) - 1
    keywd = band_list[last_item]
    # google image
    response = google_images_download.googleimagesdownload()
    absolute_img_paths = response.download({"keywords":keywd, "size":"medium",
                                            "output_directory":"./images/band",
                                            "no_directory":"true",
                                            "no_numbering":"true", "limit":1})
    path = absolute_img_paths[keywd][0]
    art = path.replace("/var/www/jessebot.io/images/band/","")

    conn = sqlite3.connect('my-next-band.db')
    c = conn.cursor()

    # timestamp!
    now = str(datetime.datetime.now())

    # Insert a row of data
    insert = '''INSERT INTO bands VALUES ('{0}','{1}','{2}')'''.format(band,
                                                                       now,
                                                                       art)
    print(insert)
    c.execute(insert)
    # Save (commit) the changes
    conn.commit()

    # close db connection
    conn.close()


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
