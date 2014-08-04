#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('fitbit.db')

with con:

    cur = con.cursor()
    cur.execute("CREATE TABLE fitbit_daily(datestamp INT PRIMARY KEY, floors INT, steps INT, miles REAL, kilometers REAL)")
