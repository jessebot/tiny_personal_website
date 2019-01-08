#!/usr/bin/env python3
# script by jessebot@linux.com to get the bands and do the things
# 1/7/19 -- 2019? D:
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

    now = datetime.datetime.now()
    
    sqlite3.register_adapter(datetime.datetime, adapt_datetime)
    conn = sqlite3.connect('bands.db')
    
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE bands
              (name text, time text)''')

    # Insert a row of data
    c.execute("INSERT INTO bands VALUES ({0},{1})".format(args.band,
                                                          now))
    
    # Save (commit) the changes
    conn.commit()
    
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

if __name__ == "__main__":
    main()
