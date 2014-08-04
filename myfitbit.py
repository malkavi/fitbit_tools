#!/usr/bin/env python

# Consultas habituales

import datetime
import simplejson as json
import time

import fitbit

class MyFitbit:
    def __init__( self ):
        print "init"

    def get_day_data(self, date='' ):
        if date == '' :
            date = datetime.date( 2014,8,1 )
        # start is agosto 1 de 2014
        weekdays = ( 'Mon' , 'Tue' , 'Wed' , 'Thu' , 'Fri' , 'Sat' , 'Sun' ) 
        data = {}
        datestr = date.strftime("%Y-%m-%d")
        fb = fitbit.make_class()
        fbr = fb.activities_date_json( datestr )
        summary         = fbr['summary']
        distances       = summary['distances']
        data['date']    = datestr
        data['floors']  = 0
        data['steps']   = summary['steps']
        data['distance_k'] = 0
                                        
        for d in distances:
            activity = d['activity']
            if activity == 'total':
                data['distance_k'] = d['distance']
        data['distance_m'] = "%.02f" % ( data['distance_k'] * 0.621371 )
        data['distance_k'] = "%.02f" % data['distance_k'] 
        return data
