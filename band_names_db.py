#!/usr/bin/env python
# script by jessebot@linux.com to get the bands and do the things
# 1/7/19 -- 2019? D:
import argparse
import subprocess
import sqlite3


def add_new_band(band):
    """
    Takes a str of a bands name and adds it to a sqlite3 db
    returns the string "Success" if all went well.
    """
    # create the band art!
    bashCommand = "./generate_band_art.py --band {0}".format(band)
    print bashCommand
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print output

    # uh, idunno
    return "Success"


def get_all_bands():
    """
    grabs all the bands from sqlite3 db
    - returns a list of tuples with 2 strings of band_name, and time_stamp
    """
    conn = sqlite3.connect('my-next-band.db')

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
    parser.add_argument('--add-band', dest='band', nargs='?', type=str,
                        help='a COOL band name')
    parser.add_argument('--get-all', dest='get_all', action='store_true',
                        help='list all cool band names')

    args = parser.parse_args()

    if args.band:
        print(add_new_band(args.band))

    if args.get_all:
        print(get_all_bands())


if __name__ == "__main__":
    main()
