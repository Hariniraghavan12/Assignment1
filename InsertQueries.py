import csv
import sqlite3
import TableCreation as t
class Insertion:
    def insertQuery(self):
        db = sqlite3.connect("C:\Users\h.a.vijayaraghavan\csvdata.db")
        cursor = db.cursor()

        csv_data = csv.reader(file('empdatafinal.csv'))
        temp=[list(i) for i in csv_data]
        for row in range(1,len(temp)):
            cursor.execute('INSERT INTO Employee(Emp_Id,First_Name,Last_Name,Gender,email,DOB,Phone,DOJ,Experience) VALUES ("{}","{}","{}","{}","{}","{}",{},"{}",{})'.format(temp[row][0],temp[row][1],temp[row][2],temp[row][3],temp[row][4],temp[row][5],temp[row][6],temp[row][7],temp[row][8]))
            cursor.execute('INSERT INTO Project1(Project_Id,Project_Name) VALUES("{}","{}")'.format(temp[row][9],temp[row][10]))
            cursor.execute('INSERT INTO Supervisor(Supervisor_Id,Supervisor_Name) VALUES("{}","{}")'.format(temp[row][11],temp[row][12]))
            cursor.execute('INSERT INTO Salary(Salary_Id,Salary,Hike) VALUES("{}",{},{})'.format(temp[row][13],temp[row][14],temp[row][15]))
            cursor.execute('INSERT INTO Employee_Project(Emp_Id,Project_Id,Supervisor_Id,Salary_Id,Rollon_date,Rolloff_date,Career_level,Work_location,Designation,FiscalYear)VALUES("{}","{}","{}","{}","{}","{}",{},"{}","{}","{}")'.format(temp[row][1],temp[row][9],temp[row][11],temp[row][13],temp[row][16],temp[row][17],temp[row][18],temp[row][19],temp[row][20],temp[row][21]))
        db.commit()
        #close the connection to the database.
        cursor.close()
        print "Done"
obj1=t.Creation()
obj1.dbCreation()
obj2=Insertion()
obj2.insertQuery()