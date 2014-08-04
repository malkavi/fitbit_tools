#!/usr/bin/env python

# Consultas habituales

import datetime
import time
import mydb

class DatabaseQueries:
    def __init__( self ):
        print "init Queries"

    def check_day(self, date='' ):
	if date == '' :
	    date = datetime.date( 2014,8,1 )
        datestr = date.strftime("%Y-%m-%d")
	db = mydb.Database()
	sql = "SELECT * FROM fitbit_daily WHERE datestamp = ? "
	out = db.db_array( sql , ( datestr, ) )
	return len(out)
	
    def insert_day_data(self, obj ):
        db = mydb.Database()
        sql = "INSERT OR REPLACE INTO fitbit_daily ( floors , steps , miles , kilometers , datestamp ) VALUES ( ? , ? , ? , ? , ? )"
        out = db.db_array(sql, ( obj['floors'], obj['steps'], obj['distance_m'], obj['distance_k'], obj['date'] ) )
