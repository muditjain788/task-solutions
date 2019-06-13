#!/usr/bin/python3
import datetime
name =input("enter name")
age=int(input("enter age"))
currentyear=int(datetime.datetime.now().year)
year=95+currentyear-age
print("hey you will turn 95 by year ",year)
