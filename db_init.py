#!/usr/bin/env python
# script by jessebot@linux.com to get the bands and do the things
# 1/10/19 -- 2019? D:
import argparse
import sqlite3
import datetime
import time

def adapt_datetime(ts):
    """
    Internet says I need dis
    """
    return time.mktime(ts.timetuple())

def main ():
    """
    Let's get it on! *cracks whip*
    """
    parser = argparse.ArgumentParser(description='Document cool band names.')
    parser.add_argument('--band', nargs='?', type=str,
                        help='a COOL band name')
    
    args = parser.parse_args()
    print((args.band))

    now = str(datetime.datetime.now())
    
    conn = sqlite3.connect('bands.db')
    
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE bands (name text, time text, image text)''')

    # Insert a row of data
    insert = '''INSERT INTO bands VALUES ('{0}','{1}','{2}')'''.format(args.band,
                                                                       now,
                                                                       "placeholder")
    c.execute(insert)
    
    # Save (commit) the changes
    conn.commit()
    
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

if __name__ == "__main__":
    main()
