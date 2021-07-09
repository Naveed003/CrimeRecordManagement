from sqlite3.dbapi2 import Date, connect
import pandas as pd
import matplotlib.pyplot as plt
import time
import sys
import sqlite3
from datetime import datetime
import random


mydb = sqlite3.connect("db.sql")
mycursor = mydb.cursor()


def print_command(Number, Message):
    print("\n", "="*Number, Message.upper(), "="*Number, "\n")


def login():
    while True:
        print_command(10, "LOGIN")
        query = "select username,password from users"
        mycursor.execute(query)
        res = mycursor.fetchall()
        response = []
        temp = []
        for i in res:
            for j in i:
                temp.append(j)
            response.append(temp)
            temp = []
        print(response)

        UserName = input("ENTER USERNAME: ")
        Password = input("ENTER PASSWORD: ")
        check = [UserName, Password]
        if check in response:
            print_command(5, "LOGIN successfull")
            break
        else:
            print_command(5, "Login FAiled")

    main()


def main():
    print("="*10, "MAIN MENU", "="*10, "\n")
    print("OPTION 1: ADD CRIME RECORD")
    print("OPTION 2: MODIFY CRIME RECORD")
    print("OPTION 3: VIEW CRIME RECORDS")
    print("OPTION 4: ADD OFFENCE TYPE")
    print("OPTION 5: MODIFY OFFENCE TYPE")
    print("OPTION 6: VIEW OFFENCE TYPES")
    print("OPTION 7: DATA VISUALIZATION")
    print("OPTION 8: CLOSE APPLICATION")
    temp = [1, 2, 3, 4, 5, 6, 7, 8]
    while True:
        response = input("\nENTER OPTION: ")
        try:
            response = int(response)
            if response in temp:
                break
            else:
                print_command(5, "ENTER VALID OPTION")

        except Exception:
            continue

    dic = {
        1: AddCrimeRec(),
        2: ModifyCrimeRec(),
        3: ViewCrimeRec(),
        4: AddOffenceType(),
        5: ModifyOffenceType(),
        6: ViewOffenceTypes(),
        7: DataVisualization(),
        8: sys.exit(),
    }

    dic[response]


def AddCrimeRec():
    query = "select RecNo from CrimeRecords"
    mycursor.execute(query)
    res = mycursor.fetchall()
    RecNos = []
    for i in res:
        for j in i:
            RecNos.append(str(j))

    query = "select OffenceNo from OffenceType"
    mycursor.execute(query)
    res = mycursor.fetchall()
    OffenceNos = []
    for i in res:
        for j in i:
            OffenceNos.append(str(j))
    print(OffenceNos)
    print(RecNos)

    while True:
        NewRecNo = random.randint(1000, 9999)
        if NewRecNo not in RecNos:
            NewRecNo = NewRecNo
            break
        else:
            continue

    CurrentDate = str(datetime.now())[0:11]

    while True:
        NewOffenceNo = input("ENTER OFFENCE NUMBER: ")

        if NewOffenceNo not in OffenceNos:
            print_command(5, "OFFENCE NUMBER INVALID")
        else:
            NewOffenceNo = int(NewOffenceNo)
            break
    while True:
        Complaint = input("COMPLAINT GIVEN BY: ")
        if Complaint != "":
            Complaint = Complaint.upper()
            break
        else:
            print_command(5, "ENTER A NAME")
    while True:
        Address = input("ADDRESS OF {}: ".format(Complaint))
        if Address != "":
            Address = Address.upper()
            break
        else:
            print_command(5, "ENTER A ADDRESS")
    while True:
        Phone = input("PHONE NUMBER OF {}: ".format(Complaint))
        if Phone != "":
            break
        else:
            print_command(5, "ENTER A PHONE NUMBER")

    while True:
        Status = input("STATUS (OPEN/CLOSED): ")
        if Status.lower() in ["open", "closed"]:
            Status = Status.upper()
            break
        else:
            print_command(5, "ENTER A VALID STATUS (OPEN/CLOSED)")

    LastUpdated = CurrentDate

    Notes = input("NOTES: ")
    query = "insert into CrimeRecords values({},'{}',{},'{}','{}','{}','{}','{}','{}')".format(
        NewRecNo, CurrentDate, NewOffenceNo, Complaint, Address, Phone, Status, LastUpdated, Notes)
    mycursor.execute(query)
    mydb.commit()
    pass


def ModifyCrimeRec():
    pass


def ViewCrimeRec():
    pass


def AddOffenceType():

    pass


def ModifyOffenceType():
    pass


def ViewOffenceTypes():
    pass


def DataVisualization():
    pass


if __name__ == "__main__":
    print_command(20, "CRIME RECORD MANAGEMent")
    AddCrimeRec()
