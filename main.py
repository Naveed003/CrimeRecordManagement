from sqlite3.dbapi2 import connect
import pandas as pd
import matplotlib.pyplot as plt
import time
import sys
import sqlite3


mysql = sqlite3.connect("db.sql")
mycursor = mysql.cursor()


def login():
    while True:
        print("="*10, "LOGIN", "="*10, "\n")
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
            print("\n", "="*5, "LOGIN SUCCESSFULL", "="*5, "\n")
            break
        else:
            print("\n", "="*5, "LOGIN FAILED", "="*5, "\n")

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
                print("\n", "="*5, "ENTER VALID OPTION", "="*5, "\n")
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
    print("="*20, "CRIME RECORD MANAGEMENT", "="*20, "\n")
    main()
