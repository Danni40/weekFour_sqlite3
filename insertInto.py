#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:49:53 2018

@author: dannilew
"""
import sqlite3
connection = sqlite3.connect("week4.db")
#adding data model
cursor = connection.cursor()
sql_command = """
CREATE TABLE people (
   id integer primary key,
   name varchar,
   position varchar,
   phone varchar,
   office varchar
);"""
cursor.execute(sql_command)
sql_command = """
CREATE TABLE experiment (
   id integer primary key,
   name varchar,
   researcher integer,
   description text,
   foreign key(researcher) references people(id)
);"""
cursor.execute(sql_command)
#adding data for people table
people_data = [ ('Alice', 'Research Director', '555-123-0001', '4b'),
               ('Bob', 'Research Assistant', '555-123-0002', '17'),
               ('Charles', 'Research Assistant', '555-123-0001', '24'),
               ('David', 'Research Assistant', '555-123-0001', '8'),
               ('Edward', 'Toadie', 'None', 'Basement')]
               
for p in people_data:
    format_str = """INSERT INTO people (id, name, position, phone, office)
    VALUES (NULL, "{name}", "{position}", "{phone}", "{office}");"""

    sql_command = format_str.format(name=p[0], position=p[1], phone=p[2], office = p[3])
    cursor.execute(sql_command)
#adding data for experiement table
experiment_data = [('EBV Vaccine trial', 0, 'A vaccine trial'),
                   ('Flu Antibody Study', 2, 'Study of the morphology of flu antibodies')]

for e in experiment_data:
    format_str = """INSERT INTO experiment ( id, name, researcher, description)
    VALUES (NULL, "{name}", "{researcher}", "{description}");"""
    
    sql_command = format_str.format(name=e[0], researcher=e[1], description=e[2])
    cursor.execute(sql_command)
#commit the changes
connection.commit()
connection.close()  #close the connection