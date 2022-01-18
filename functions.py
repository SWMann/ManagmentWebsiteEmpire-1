
import psycopg2
import psycopg2.extras
import requests
import json
import yaml
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

db2 = yaml.load(open('info.yaml'), Loader=yaml.FullLoader)
DB_Host = db2["DB_Host"]
DB_Name = db2["DB_Name"]
DB_User = db2["DB_User"]
DB_Pass = db2["DB_Pass"]
DB_Port = db2["DB_Port"]
DB_Expected = db2["DB_Expected"]

## Functions Library ##

def GetAllMembers():
    con = psycopg2.connect(dbname=DB_Name, user=DB_User, password=DB_Pass, host=DB_Host, port=DB_Port)
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("SELECT * FROM \"EmpireManagmentWebsite\".\"Members\"")

    Members=cur.fetchall()

    con.close()
    return Members

def GetAMember(Name):
    Members = GetAllMembers()
    for x in Members:
        print(x[1])
        if x[1] == Name:
            print("Found Them!")
            return x
            break
    print("Could not find that user")

def GetAllCapitalShips():
    con = psycopg2.connect(dbname=DB_Name, user=DB_User, password=DB_Pass, host=DB_Host, port=DB_Port)
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("SELECT * FROM \"EmpireManagmentWebsite\".\"Capital Ships\"")

    CapitalShips=cur.fetchall()

    con.close()

    return CapitalShips

def GetACapitalShip(Name):
    Capitals = GetAllCapitalShips()
    for x in Capitals:
        print(x[1])
        if x[1] == Name:
            print("Found It!")
            return x
            break
    print("Could not find that Capital ship")