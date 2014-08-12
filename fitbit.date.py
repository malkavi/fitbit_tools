#!/usr/bin/env python

# pull all fitbit data from Fitbit API to MySQL server

# June 20th is my first day with a FitBit. fill in yours

import datetime 
import httplib
import os
import simplejson as json
import time
from oauth import oauth

import myfitbit
import dbqueries

def main():
    date = datetime.datetime( 2014,8,01,1,0,0 )
    now = datetime.datetime.now()
    c = 1
    
    queries = dbqueries.DatabaseQueries()
    fitbit = myfitbit.MyFitbit()
    
    while date < now:
        a = []
        a.append('')
        a.append(str(c))
        a.append(date.strftime("%Y-%m-%d"))
        check = queries.check_day( date )
        if check != 1 :
            queries.insert_day_data( fitbit.get_day_data( date ) )
        date = date + datetime.timedelta(1)

if __name__ == '__main__':
    main()
