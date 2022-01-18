## Testing API functionality ###
import psycopg2
import psycopg2.extras
import functions
import requests
import json
import yaml
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


## Connection Setup ##
db2 = yaml.load(open('info.yaml'), Loader=yaml.FullLoader)
DB_Host = db2["DB_Host"]
DB_Name = db2["DB_Name"]
DB_User = db2["DB_User"]
DB_Pass = db2["DB_Pass"]
DB_Port = db2["DB_Port"]
DB_Expected = db2["DB_Expected"]
db = SQLAlchemy(app)



## Connection Test ##
print("Attempting to Connect")
con = psycopg2.connect(dbname=DB_Name,user=DB_User,password=DB_Pass,host=DB_Host,port=DB_Port,connect_timeout=3)
cur = con.cursor()
cur.execute('SELECT version()')
version = cur.fetchone()[0]

if DB_Expected in version:
    print("Connection was verified")
    print("")

else:
    print("Connection could not be verified, proceed with caution")
    print(version)
con.close()

## Connection Test 2 ##

print(functions.GetAllMembers())



## Models ##
    # TODO: Setup intergration with postgres
class Member(db.Model):
    __tablename__ = 'Members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    Membership = db.Column(db.String(20))
    Rank = db.Column(db.String(30))

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.Membership} - {self.Rank}"



## Routes ##

@app.route('/')
def index():
    con = psycopg2.connect(dbname=DB_Name, user=DB_User, password=DB_Pass, host=DB_Host, port=DB_Port)
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("SELECT * FROM \"EmpireManagmentWebsite\".\"Members\"")

    Members=cur.fetchall()
    print(Members)
    con.close()
    return str(Members)




Member = functions.GetAMember("Qrahn")

print(Member)

Capitals = functions.GetAllCapitalShips()

print(functions.GetACapitalShip("Reliance"))
