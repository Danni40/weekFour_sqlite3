#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("week4.db")

cursor = connection.cursor()
#select all from people to verify data
cursor.execute("SELECT * FROM people") 
print("All People")
result = cursor.fetchall() 
for r in result:
    print(r)
#select all from experiment to verify data
cursor.execute("SELECT * FROM experiment") 
print("All Experiements:")
result = cursor.fetchall() 
for r in result:
    print(r)
#have it print out all of the experiment names with who owns each experiment
r2 = cursor.execute("select p.name, e.name from people as p join experiment as e where e.researcher == p.id;")
#'select p.name, e.name from people as p join experiment as e where e.researcher == p.id'
for i in r2:
    print('Name: %s\n\tExperiment: %s' % (i[0],i[1]))
connection.close()