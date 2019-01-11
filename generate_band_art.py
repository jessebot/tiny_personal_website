#!/usr/bin/env python3
# script by jessebot@linux.com to get the bands' art and do the things
# 1/10/19 -- 2019? D:
import argparse
from google_images_download import google_images_download


def generate_band_art(band):
    # change image results by making different key words
    band_list = band.split()
    last_item = len(band_list) - 1
    keywd = band_list[last_item]
    # google image
    response = google_images_download.googleimagesdownload()
    absolute_img_paths = response.download({"keywords":keywd, "size":"medium",
                                            "output_directory":"./images/band",
                                            "no_directory":"true", "limit":1})
    print(type(absolute_img_paths))
    print(absolute_img_paths)


def main():
    parser = argparse.ArgumentParser(description='Document cool band names.')
    parser.add_argument('--add-band', dest='band', nargs='?', type=str,
                        help='a COOL band name')
    parser.add_argument('--get-all', dest='get_all', action='store_true',
                        help='list all cool band names')

    args = parser.parse_args()

    if args.band:
        generate_band_art(args.band)

if __name__ == '__main__':
    main()
