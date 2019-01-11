#!/usr/bin/env python
# script by jessebot@linux.com to get the bands and do the things
# 1/7/19 -- 2019? D:
import argparse
import datetime
import random
import sqlite3


def generate_band_art(band):
    categories = ['abstract', 'animals', 'business', 'cats', 'city', 'food',
                  'night', 'life', 'fashion', 'people', 'nature', 'sports',
                  'technics', 'transport']
    category = random.choice(categories)
    url = "http://lorempixel.com/400/400/{0}/{1}".format(category, band)
    

def add_new_band(band):
    """
    Takes a str of a bands name and adds it to a sqlite3 db
    returns the string "Success" if all went well.
    """
    now = str(datetime.datetime.now())

    conn = sqlite3.connect('bands.db')
    c = conn.cursor()

    # Insert a row of data
    insert = '''INSERT INTO bands VALUES ('{0}','{1}')'''.format(band, now)
    try:
        c.execute(insert)
        # Save (commit) the changes
        conn.commit()
    except Exception as e:
        return e

    # close connection
    conn.close()

    # uh, idunno
    return "Success"


def get_all_bands():
    """
    grabs all the bands from sqlite3 db
    - returns a list of tuples with 2 strings of band_name, and time_stamp
    """
    conn = sqlite3.connect('bands.db')

    c = conn.cursor()

    # Insert a row of data
    get = '''SELECT * FROM bands'''
    c.execute(get)

    # print(c.fetchall())
    all_bands = c.fetchall()

    # close connection
    conn.close()

    return all_bands


def main():
    """
    Let's get it on! *cracks whip*
    """
    parser = argparse.ArgumentParser(description='Document cool band names.')
    parser.add_argument('--band', nargs='?', type=str,
                        help='a COOL band name')
    parser.add_argument('--get-all', dest='get_all', action='store_true',
                        help='list all cool band names')

    args = parser.parse_args()

    if args.band:
        print add_new_band(args.band)

    if args.get_all:
        print get_all_bands()


if __name__ == "__main__":
    main()
