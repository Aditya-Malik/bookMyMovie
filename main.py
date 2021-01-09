# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:17:56 2021

@author: adity
"""
from db import dbnew, dbcon
global row
global seats

while (True) :
    
    db = input("Do you want to create new schema or use existing one? (new/existing)\n")
    db.lower()
    
    if db == "new":
        dbnew()
        row=int(input("Enter the number of rows: "))
        seats=int(input("Enter number of seats in each row: "))
        with open("rows_and_seats.txt","w+") as fp:
            fp.write(str(row)+" ")
            fp.write(str(seats))
            fp.close()
        break
    elif db == "existing":
        dbcon()
        with open("rows_and_seats.txt","r+") as fp:
            content = fp.read()
            row = int(content[0])
            seats = int(content[2])
            fp.close()
        print("Number of rows were:",row)
        print("Seats in each row were:",seats)
        break

from cinema import Cinema 

while (True) :
    
    catalog = input("1. Show Seats\n2. Buy Ticket\n3. View Statistics\n4. Show Booked Tickets Customer Info\n0. Exit\n\n")
    obj = Cinema()
    
    if catalog == "1":
        obj.show_seats(row,seats)

    elif catalog == "2":
        obj.buy_ticket(row,seats)

    elif catalog == "3":
        obj.show_statistics(row,seats)

    elif catalog == "4":
        obj.show_booked_ticket()

    elif catalog == "0":
        break