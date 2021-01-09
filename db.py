def dbnew():
        
    import mysql.connector as myc
        
    try:
        # Connect to mysql
        cnx = myc.connect(host="localhost",user="root",passwd="")
        mycursor = cnx.cursor()
        # Creation of database
        mycursor.execute("DROP DATABASE IF EXISTS cinemaproj;")
        cnx.commit()
        mycursor.execute("CREATE DATABASE cinemaproj;")
        cnx.commit()
        mycursor.execute("USE cinemaproj;")
        # Creation of customer table
        mycursor.execute("CREATE TABLE customer(cid INT AUTO_INCREMENT, Name VARCHAR(25),Gender VARCHAR(15),Age INT,phone_number VARCHAR(13),seat_no INT UNIQUE,ticket_price INT, PRIMARY KEY (cid));")
        cnx.commit()
            
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
            
    finally:
        print("Database Schema Created!")
        cnx.close()



def dbcon():
        
    import mysql.connector as myc
        
    try:
        # Connect to mysql
        cnx = myc.connect(host="localhost",user="root",passwd="")
        mycursor = cnx.cursor()
        # Pick database to use
        mycursor.execute("USE cinemaproj;")
            
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
            
    finally:
        print("Database Successfully Imported!")
        cnx.close()