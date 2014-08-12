#!/usr/bin/env python

# downloads last five days of fitbit info, not including the current day.
# the current day's info isn't finished, and I often don't have it sync
# during the weekend

import datetime 
import httplib
import os
import simplejson as json
import time
from oauth import oauth

import myfitbit
import dbqueries

def main():
    #date = datetime.datetime( 2014,8,04,14,22,0 )
    date = datetime.datetime.now()
    
    queries = dbqueries.DatabaseQueries()
    fitbit = myfitbit.MyFitbit()
    
    for i in range(0,5):
    	print date
        date = date - datetime.timedelta(1)
        queries.insert_day_data( fitbit.get_day_data(date) )

if __name__ == '__main__':
    main()
