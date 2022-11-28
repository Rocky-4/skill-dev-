#!/usr/bin/python
import pymysql
import csv
conn = pymysql.connect(host='localhost', user='roshan', password = "roshan9869", db='curd')
cur = conn.cursor(pymysql.cursors.DictCursor);




def updateData():
    user_id = int(input("Enter id: "));
    user_name = input("Enter name: ");
    user_age = int(input("Enter age: "));    
    try:
    	sql = "UPDATE student SET Name =%s , Age =%s WHERE ID =%s "
    	cur.execute(sql,(user_name,user_age,user_id));
    	conn.commit();
    	showData();
      	
    except pymysql.err.IntegrityError :
    	print("\n\t!!!!!!!!!!!!!!Failed .........Repeted ID")
    except:
    	print("\n\tFormat Error")


def insertData():
    user_name = input("Enter name: ");
    user_age = int(input("Enter age:"))
    user_id = input("Enter ID: ");
    
    try:
    	sql = ("INSERT INTO student (ID, Name, Age) VALUES(%s ,%s ,%s)")
    	cur.execute(sql,(user_id,user_name,user_age));
    	conn.commit();
    	showData();
    except pymysql.err.IntegrityError :
    	print("\n\t!!!!!!!!!!!!!!Failed .........Repeted ID")
    except:
    	print("\n\tFormat Error")


def deleteData():
    user_id = int(input("Enter id to delete record: "));
    
    try:
    	sql = f"DELETE FROM student WHERE ID = {user_id}";
    	cur.execute(sql);
    	conn.commit();
    	showData();
    except:
    	print("\n\tFormat Error")


def showData():
    sql = "SELECT * FROM student";
    cur.execute(sql)
    records = cur.fetchall()
    print(records); #this will print list
    return records;


option = None;

while(option != 0):
    print("\n================\n");
    print("1. Show Data");
    print("2. Detele data");
    print("3. Insert data");
    print("4. Update data");
    print("0. Exit");

    option = int(input("Choose Option: "));

    if(option == 1):
        showData();


    if(option == 2):
        deleteData();


    if(option == 3):
        insertData();

    if(option == 4):
        updateData();

    if(option == 0):
        print("Exiting");
