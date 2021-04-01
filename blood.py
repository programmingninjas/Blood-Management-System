import mysql.connector as ms
import login

def add_donor():
    while True:
        choice = input('Do you want to add a donor? (y/n) ')
        if choice.lower() == 'y':
            cursor.execute("CREATE TABLE IF NOT EXISTS blood(ID INT AUTO_INCREMENT,Donor_Name VARCHAR(20),Age INT,Gender VARCHAR(10),Blood_Group VARCHAR(3),Diabetic VARCHAR(10),Any_Other_Diseases VARCHAR(100),PRIMARY KEY(Id))")
            cursor.execute("CREATE TABLE IF NOT EXISTS rejected_blood(ID INT AUTO_INCREMENT,Donor_Name VARCHAR(20),Age INT,Gender VARCHAR(10),Blood_Group VARCHAR(3),Diabetic VARCHAR(10),Any_Other_Diseases VARCHAR(100),PRIMARY KEY(Id))")
            name = input("Enter Donor's Name: ")
            age =  input("Enter Donor's Age: ")
            gender = input("Enter Donor's Gender: ")
            group = input("Enter Donor's Blood Group: ")
            pronoun = 'he' if gender.lower() == 'male' else 'she' 
            diabetic = input("Is {x} diabetic? (yes/no)".format(x=pronoun))
            other = input("If any other disease mention (leave blank if not): ")
            print("\n")
            if diabetic.lower() == 'yes' or bool(other):
                cursor.execute("INSERT INTO rejected_blood (Donor_Name,Age,Gender,Blood_Group,Diabetic,Any_other_diseases) VALUES(%s,%s,%s,%s,%s,%s)",(name,age,gender,group,diabetic,other))
                database.commit()
            else:
                cursor.execute("INSERT INTO blood (Donor_Name,Age,Gender,Blood_Group,Diabetic,Any_other_diseases) VALUES(%s,%s,%s,%s,%s,%s)",(name,age,gender,group,diabetic,other))
                database.commit()
        else:
            driver()
def display_donor():
    while True:
        print(" 1) Display All Records",'\n',"2) Display Particular Record",'\n',"3) Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            cursor.execute("SELECT * FROM blood")
            data = cursor.fetchall()
            for i in data:
                print('\n')
                for j in range(6):
                    headings = ['Donor_Name: ','Age: ','Gender: ','Blood_Group: ','Diabetic: ','Any_other_disease: ']
                    print(i[0],')','\t',headings[j],i[j+1]) if j == 0 else print('\t',headings[j],i[j+1])
            else:
                print('\n')
        if choice == '2':
            name = input("Enter Donor's Name: ")
            cursor.execute("SELECT * FROM blood WHERE Donor_Name='{x}'".format(x=name))
            data = cursor.fetchall()
            for i in data:
                print('\n')
                for j in range(6):
                    headings = ['Donor_Name: ','Age: ','Gender: ','Blood_Group: ','Diabetic: ','Any_other_disease: ']
                    print(i[0],')','\t',headings[j],i[j+1]) if j == 0 else print('\t',headings[j],i[j+1])
            else:
                print('\n') 
        if choice == '3':
            driver()
def display_rejected_donor():
    while True:
        print(" 1) Display All Rejected Records",'\n',"2) Display Particular Rejected Record",'\n',"3) Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            cursor.execute("SELECT * FROM rejected_blood")
            data = cursor.fetchall()
            for i in data:
                print('\n')
                for j in range(6):
                    headings = ['Donor_Name: ','Age: ','Gender: ','Blood_Group: ','Diabetic: ','Any_other_disease: ']
                    print(i[0],')','\t',headings[j],i[j+1]) if j == 0 else print('\t',headings[j],i[j+1])
            else:
                print('\n')
        if choice == '2':
            name = input("Enter Donor's Name: ")
            cursor.execute("SELECT * FROM rejected_blood WHERE Donor_Name='{x}'".format(x=name))
            data = cursor.fetchall()
            for i in data:
                print('\n')
                for j in range(6):
                    headings = ['Donor_Name: ','Age: ','Gender: ','Blood_Group: ','Diabetic: ','Any_other_disease: ']
                    print(i[0],')','\t',headings[j],i[j+1]) if j == 0 else print('\t',headings[j],i[j+1])
            else:
                print('\n') 
        if choice == '3':
            driver()
def remove_donor():
    while True:
        print(" 1) Remove Particular Record",'\n',"2) Remove All Records",'\n',"3) Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter Donor's Name: ")
            Id = int(input("Enter Donor's Id: "))
            cursor.execute("DELETE FROM blood WHERE Donor_Name='{x}' AND Id={y}".format(x=name,y=Id))
            database.commit()
            print('\n','Record Removed Successfully!')
        if choice == '2':
            warn = input("Are you sure? Type 'yes' or 'no': ")
            if warn == 'yes':
                cursor.execute("TRUNCATE TABLE blood")
                database.commit()
                print("All Records Removed Successfully!")
            else:
                remove_donor()
        if choice == '3':
            driver()
def remove_rejected_donor():
    while True:
        print(" 1) Remove Particular Rejected Record",'\n',"2) Remove All Rejected Records",'\n',"3) Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter Donor's Name: ")
            Id = int(input("Enter Donor's Id: "))
            cursor.execute("DELETE FROM rejected_blood WHERE Donor_Name='{x}' AND Id={y}".format(x=name,y=Id))
            database.commit()
            print('\n','Record Removed Successfully!')
        if choice == '2':
            warn = input("Are you sure? Type 'yes' or 'no': ")
            if warn == 'yes':
                cursor.execute("TRUNCATE TABLE rejected_blood")
                database.commit()
                print("All Records Removed Successfully!")
            else:
                remove_donor()
        if choice == '3':
            driver()
def driver():
    if flag:
        global database,cursor
        database = ms.connect(host='localhost', user='root',passwd='root',database='data')
        cursor = database.cursor()
        print(" 1) Add Donor",'\n',"2) Display Donor",'\n',"3) Display Rejected Donor",'\n',"4) Remove Donor",'\n',"5) Remove Rejected Donor",'\n',"6) Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_donor()
        if choice == '2':
            display_donor()
        if choice == '3':
            display_rejected_donor()
        if choice == '4':
            remove_donor()
        if choice == '5':
            remove_rejected_donor()
        if choice == '6':
            quit()
flag = login.main()
driver()
            
