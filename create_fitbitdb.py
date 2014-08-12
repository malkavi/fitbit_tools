#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('fitbit.db')

with con:

    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS fitbit_daily(datestamp INT PRIMARY KEY, floors INT, steps INT, miles REAL, kilometers REAL)")
    #weight table
    cur.execute("CREATE TABLE IF NOT EXISTS weight(CURRENT_DATE DATETIME PRIMARY KEY NOT NULL  DEFAULT (CURRENT_DATE), weight REAL)")
    cur.execute("INSERT OR REPLACE INTO weight (CURRENT_DATE, weight) VALUES (DATE('now'), 85.2)")
