import mysql.connector

#	CREATE A NEW TABLE
def create_type_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS type_tb (TypeID INT AUTO_INCREMENT, TypeName VARCHAR(30), Role VARCHAR(30), WeightCapacity INT, CONSTRAINT TypeID_pk PRIMARY KEY (TypeID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_type_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT TYPES IN THE COMMAND DATABASE
def insert_Type(mycursor, TypeName, Role, WeightCapacity):
	#need to verify that the TypeName is an existing Type in the Type database
	sql="INSERT INTO type_tb (TypeName, Role, WeightCapacity) VALUES(%s,%s,%s)"
	val=(TypeName, Role, WeightCapacity)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"type ajouté")

#	GET ALL POSSIBLE TYPES
def get_all_Type(mycursor):
	sql="SELECT * FROM type_tb ORDER BY TypeName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET A TYPE BY ITS NAME
def get_Type_by_name(mycursor, TypeName):
	sql = "SELECT * FROM type_tb WHERE TypeName=TypeName IF EXISTS"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A TYPE
def delete_Type(mycursor, TypeName):
	sql="DELETE FROM type_tb WHERE TypeName=TypeName"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Type deleted")

def delete_flotte_db(mycursor):
	sql="DROP DATABASE flotte_db"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED **explosion**")


