# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:36:14 2021

@author: adity
"""
import mysql.connector as myc
import math

cnx = myc.connect(host="localhost",user="root",passwd="", database = "cinemaproj")
mycursor = cnx.cursor()

class Cinema():
    
    def show_seats(self,row,seats):
        
        global tickets_booked
        tickets_booked = 0
        print("Cinema:")
        for i in range(row+1):
            for j in range(seats+1):
                if i == 0:
                    if i == j == 0:
                        print(" ",end = " ")
                        continue
                    else:
                        print(j, end= " ")
                else:
                    if i == 1 and j == 0:
                        print("")
                    else:
                        count = 1
                        print(i , end= " ")
                        while(True):
                            if count <= seats:
                                seat_no = int(str(i)+str(count))
                                sql = 'select * from customer where seat_no = %s'
                                val = (seat_no,)
                                mycursor.execute(sql,val)
                                res = mycursor.fetchone()
                                if res:
                                    print("B", end=" ")
                                    tickets_booked += 1
                                else:
                                    print("S", end=" ")
                                count = count + 1
                            else:
                                print("")
                                break
                        break
    
    
    
    def buy_ticket(self, row, seats):
        
        s_row = int(input("Enter row number:"))
        s_col = int(input("Enter seat number:"))
        s_seat_no = int(str(s_row) + str(s_col))
        sql="SELECT seat_no FROM customer;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        global seat_status
        seat_status = "Available"
        for i in res:
            if s_seat_no in i:
                print("Seat already booked! Kindly see arrangement and book an unreserved seat!")
                seat_status = "Booked"
                break
        if seat_status == "Available":
            if s_row <= row and s_col <= seats:
                seat_no = int(str(s_row) + str(s_col))
                ticket_price = 0
                total_seats = row * seats
                if total_seats <= 60:
                    ticket_price = 10
                else:
                    division = row / 2
                    f_row = math.floor(division)
                    if s_row <= f_row:
                        ticket_price = 10
                    else:
                        ticket_price = 8
                print("Ticket price :", ticket_price)

                prompt = input("Do you want to Book the ticket (yes/no):")
                ans = prompt.lower()
                if ans == "yes":
                    print("Kindly Enter details\n")
                    name = input("Your Name:")
                    gender = input("Gender:")
                    age = int(input("Age:"))
                    phone = input("Phone number:")
                    sql = "insert into customer(Name,Gender,Age,phone_number,seat_no,ticket_price) values (%s,%s,%s,%s,%s,%s);"
                    val = (name, gender, age, phone, seat_no, ticket_price)
                    mycursor.execute(sql, val)
                    cnx.commit()
                    mycursor.execute('select * from customer where Name = name')
                    res = mycursor.fetchall()
                    if res:
                        print("Ticket Booked Successfully!")
                    else:
                        print("ERROR! Please try again after sometime.")
                else:
                    print("Booking Cancelled.")
            else:
                print("Seat does not exist! Enter a valid seat number next time.")
    
            
    
    def show_statistics(self,row,seats):
        
        global total_income
        total_income = 0
        sql="SELECT count(*) from customer;"
        mycursor.execute(sql)
        tickets_booked_list = mycursor.fetchall()
        tickets_booked = tickets_booked_list[0][0]
        print("Number of tickets purchased:",tickets_booked)
        total_seats = row * seats
        percentage_of_tickets_booked = (tickets_booked / total_seats) * 100
        print("Percentage of tickets booked:",str(round(percentage_of_tickets_booked,2))+"%")
        max_seat = int(str(row) + str(seats))
        sql = "select sum(ticket_price) from customer where seat_no <= %s"
        val = (max_seat,)
        mycursor.execute(sql,val)
        res = mycursor.fetchone()
        for price in res:
            print("Current Income:","$"+str(price))
        res = row * seats
        if res <= 60:
            total_income = 10 * seats * row
        else:
            res = row / 2
            division_row = math.floor(res)
            premium_tickets_price = 10 * seats * division_row  # formula = price * number of columns * number of rows
            normal_tickets_rows = row - division_row
            normal_tickets_price = 8 * seats * normal_tickets_rows
            total_income = premium_tickets_price + normal_tickets_price
        print("Total Possible Income:","$"+str(total_income))
    

                
    def show_booked_ticket(self):
        
        ans=input("Do you want to see all customer info or a particular seat customer (all/customer) ?\n")
        Ans=ans.lower()
        
        if Ans=="all":
            sql = "select Name,Gender,Age,ticket_price,phone_number from customer;"
            mycursor.execute(sql)
            all_customer_info = mycursor.fetchall()
            if all_customer_info:
                customer_number=0
                for customer in all_customer_info:
                    customer_number+=1
                    print(str(customer_number)+".)")
                    print("Name:",customer[0])
                    print("Gender:",customer[1])
                    print("Age:",customer[2])
                    print("Ticket Price:" + str(customer[3]) + "$")
                    print("Phone Number:",customer[4],"\n")
            else:
                print("No bookings made till now!")
                
        elif Ans=="customer":
            s_row = int(input("Enter row:"))
            s_col = int(input("Enter col:"))
            sno = int(str(s_row) + str(s_col))
            sql = "select Name,Gender,Age,ticket_price,phone_number from customer where seat_no = %s;"
            val = (sno,)
            mycursor.execute(sql, val)
            customer_info = mycursor.fetchone()
            if customer_info:
                print("Name:", customer_info[0])
                print("Gender:", customer_info[1])
                print("Age:", customer_info[2])
                print("Ticket Price:", str(customer_info[3]) + "$")
                print("Phone Number:", customer_info[4])
            else:
                print("No booking for this seat.\n")
                
        else:
            print("Invalid input!\n")
