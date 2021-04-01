import mysql.connector as ms

def main():    
    try:
        #Creating DataBase
        database = ms.connect(host='localhost', user='root',passwd='root')
        cursor = database.cursor()
        cursor.execute("CREATE DATABASE data")        
        cursor.close()
        database.close()
        #Connecting DataBase
        database = ms.connect(host='localhost',user='root',passwd='root',database='data')
        cursor = database.cursor()
        print("-"*20,">Welcome to Blood Management System<","-"*19,'\n'*2,'\t'*2,"Please set your username and password",'\n')
        cursor.execute("CREATE TABLE login(Username VARCHAR(30),Password VARCHAR(20))")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        cursor.execute("INSERT INTO login VALUES(%s,%s)",(username,password))
        database.commit()
        cursor.close()
        database.close()
        main()        
    except:
        #Connecting DataBase
        database = ms.connect(host='localhost', user='root',passwd='root',database='data')
        cursor = database.cursor()
        print("-"*20,">Welcome to Blood Management System<","-"*19,'\n'*2,'\t'*2,"Please Enter your username and password to login",'\n')
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        cursor.execute("SELECT * FROM login")
        data = cursor.fetchall()
        u_name = data[0][0]
        passwd = data[0][1]
        if [username,password] == [u_name,passwd]:
            return True
        else:
            main()



    

    

    
