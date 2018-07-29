# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 13:48:09 2018

@author: Danni Lewis
"""
#import the module
import sqlite3
#connect or create a local db
connection = sqlite3.connect("week4.db")
#run connection functions
cursor = connection.cursor()
#insert more experiment assignments
sql_command = """
INSERT INTO experiment values ( Null, 'EBV Vaccine trial', 1, 'A vaccine trial');
"""
#execute the sql command
cursor.execute(sql_command)
sql_command = """
INSERT INTO experiment values ( Null, 'Flu Antibody Study', 3, 'Study of the morphology of flu antibodies');
"""
cursor.execute(sql_command)
sql_command = """
INSERT INTO experiment values ( Null, 'EBV Vaccine trial', 5, 'Study of the morphology of flu antibodies');
"""
cursor.execute(sql_command)
sql_command = """
INSERT INTO experiment values ( Null, 'Flu Antibody Study', 6, 'Study of the morphology of flu antibodies');
"""
cursor.execute(sql_command)
sql_command = """
INSERT INTO experiment values ( Null, 'Flu Antibody Study', 4, 'Study of the morphology of flu antibodies');
"""
cursor.execute(sql_command)
#add new user
sql_command = """
INSERT INTO people values ( Null, 'Danni', 'Research Executive', '555-123-1000', '35F');
"""
#execute the sql command
cursor.execute(sql_command)
#delete Alice
sql_command = """
DELETE FROM people where name="Alice";
"""
cursor.execute(sql_command)
#assign Alice's assignments to the new user
sql_command = """
UPDATE experiment set name='EBV Flu Antibody Study' where id=6;
"""
cursor.execute(sql_command)
#commit all sql commands
connection.commit()
connection.close()