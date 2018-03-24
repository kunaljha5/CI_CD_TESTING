#!/usr/bin/env python
#
#	BMI Calculator
#	Created by Kunal Jha
#	Dated:	08/March/2018
#	This script will genrate BMI report for the end user along with that  
#	DB Name is BMI
#	Table Name is BMI
#	USER kunal jha05
#	password base64 encoded
#	each user request will be entered in mysql DB using insert query
#
# 
######################################
import base64
import os
import MySQLdb
import getopt
import sys
import boto3


class encode_decode:
	
	def decode (self,encoded_string):
		self.decoded_string = base64.b64decode(encoded_string)
		return self.decoded_string
	def encode (self,decoded_string):
		self.encoded_string = base64.b64encode( decoded_string)
		return self.encoded_string

	
class Database:
    ED = encode_decode()
    host = 'localhost'
    user = 'root'
    password = 'dWJ1bnR1'
    password = ED.decode(password)
    db = 'BMI'
    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()
    def insert(self, query):
        try:
#            print "Inside the class function"
            self.cursor.execute(query)
            self.connection.commit()
#            print "completed the class function"
        except:
            self.connection.rollback()
    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)
        return cursor.fetchall()
    def __del__(self):
        self.connection.close()



def foot_to_centi(F,I):
    Foot = F*12
    Inch = I
    Inch_T = Foot + Inch
    Meter =float(Inch_T*2.54)/100
    Meter = round(Meter,2)
    return Meter

def ideal_weight(BMI,Meter):
	New_Meter= Meter**2
	Mass_now = BMI * New_Meter
	Standard_Mass = 24.9 * New_Meter
	Mass_o = Standard_Mass - Mass_now
	Mass_o = round(Mass_o,2)
	if Mass_o > 0:
		statement = "Need to increase weight by : " + str(Mass_o)
	else:
		statement = "Need to decrease weight by : " + str(Mass_o*-1) + " Kg"
	return statement





os.system('cls' if os.name == 'nt' else 'clear')
arrow =  len(sys.argv)


options, remainder = getopt.getopt(sys.argv[1:], 'n:h:w:m', ['name=', 
	                                         'height=',
	                                         'weight=',
	                                         'msisdn=',
	                                         ])
for opt, arg in options:
    if opt in ('--n', '--name'):
        name = arg
    elif opt in ('--h', '--height'):
        height = arg
    elif opt in ('--w', '--weight'):
        weight = arg
    elif opt in ('--m', '--msisdn'):
        msisdn = arg

MSISDN=msisdn
Name = name
Mass = float(weight)

try:
	F = int(height[0])
	I = int(height[2:4])
	#print I , F
except TypeError:
	print "Proivided Value is not correct . kindly insert Data in Foot,Inches i.e 5,1"
	
	

Meter =foot_to_centi(F,I)
BMI = Mass/Meter**2
BMI = round(BMI,2)
if BMI < 15 :
	cate = "Very severely underweight"
	statement = ideal_weight(BMI,Meter)
if BMI < 16 and BMI >= 15:
	cate = "Severely underweight"
	statement = ideal_weight(BMI,Meter)
if BMI < 18.5 and BMI >= 16:
	cate = "Underweight"
	statement = ideal_weight(BMI,Meter)
if BMI <= 25 and BMI >= 18.5:
	cate = "Normal"
	statement = "You are totally fit"
if BMI < 30 and BMI > 25:
	cate = "Overweight"
	statement = ideal_weight(BMI,Meter)
if BMI < 35 and BMI >= 30:
	cate = "Obese Class I"
	statement = ideal_weight(BMI,Meter)
if BMI < 40 and BMI >= 35:
	cate = "Obese Class II"
	statement = ideal_weight(BMI,Meter)
if BMI > 40:
	cate = "Obese Class III"
	statement = ideal_weight(BMI,Meter)
print '+---------------------------------------------------------------------------------------------+\
\n|\t\t\tName\t\t: '+Name + ' \t\t\t\t \
\n|\t\t\tWeight\t\t: '+str(Mass)+' Kg \t\t\t\t \
\n|\t\t\tHeight\t\t: '+str(Meter)+' Mtr \t\t\t\t \
\n|\t\t\tBMI\t\t: '+str(BMI)+' \t\t\t\t \
\n|\t\t\tCategory\t: '+str(cate)+'\t\t\t\t \
\n|\t\t\tNote\t\t: '+str(statement)+'\t\t\t\t \
\n+---------------------------------------------------------------------------------------------+' 
print ""


message1 = 'Name= ' + Name + ',\nWeight= ' + str(Mass) + ' Kg '+ ',\nHeight= ' + str(Meter) + ' Mtr ' + ',\nBMI= ' + str(BMI) + ' '+  ',\nCategory= ' + str(cate) + ' '+   ',\nNote= ' + str(statement) + '.'

if MSISDN != "":
	db = Database()
	query = """INSERT INTO BMI_SMS ( id,TIMESTAMP1, name,Height,Weight,BMI,Category,Note,MSISDN ) VALUES ( null, NOW(),'%s', '%s', '%s' , '%s', '%s', '%s','%s')"""% (Name, str(Meter),str(Mass), str(BMI), str(cate), str(statement),str(MSISDN))
	db.insert(query)
	client = boto3.client(
	    "sns",
	    aws_access_key_id="AKIAIWJY7UKWVNDLJYIQ",
	    aws_secret_access_key="do8RH+wXMu7widJKk5HGFEjV/ORS1h5pKpWuxZwg",
	    region_name="us-east-1"
	)
	# Send your sms message.
	client.publish(
	    PhoneNumber=MSISDN,
	    Message=message1
	)
else:
	db = Database()
	query = """INSERT INTO BMI_SMS ( id,TIMESTAMP1, name,Height,Weight,BMI,Category,Note,MSISDN ) VALUES ( null, NOW(),'%s', '%s', '%s' , '%s', '%s', '%s','%s')"""% (Name, str(Meter),str(Mass), str(BMI), str(cate), str(statement),str(MSISDN))
	db.insert(query)


