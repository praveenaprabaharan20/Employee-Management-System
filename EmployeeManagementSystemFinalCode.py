#Employee Management System in Python for getting the credentials of the employee such as 
#employee ID, name, phone number etc. and validating it 
#Author : Praveena
#Created Date: 16-Aug-2021
#Edited on: 17-Aug-2021
#Edited by: Praveena

#Importing essential libraries

import re
import datetime

# Function to Set the Qualification

def switchqualification(arg):
    switcher={
        1 :  "BTech Information Technology",2:"BE Computer Science",3:"BE Mechanical",4:   "BE Automobile",5:" BE EEE",6 :  "BE ECE",7 :  "BTech BioMedical",
        8 :  "Others"
              }
    return switcher.get(arg)

# Function to find repetition of characters

def findrepeated(ename):
    for i in range (0,len(ename)-2):
           if ename[i]==ename[i+1] and ename[i+1]==ename[i+2]:
               return True
    return False

# Function to find the age and experience

def findage(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# Function to Validate Employee ID

def validateemployeeID(distinctID):
    while True:
        ID=input('Enter your Employee ID in 4 digits (eg:1234):')

        if ID in distinctID:
            print("Give a distint ID.The ID you entered already exists")
            continue
        elif (not(ID.isdigit())):
            print('Oops :( ! ID should be in numeric. Try again')
            continue
        elif int(ID)==0:
            print('Oh-no! Employee ID cannot be null. Please enter  valid ID')
            continue
        elif len(ID)!=4:
            print('Oh-no! Employee ID contain must 4 characters. Enter zeroes before if it is a single ,double or triple digit number')
            continue
        else:
            distinctID.append(ID)
            EmpID= 'ACE'+ID
            return EmpID

# Function to Validate Employee Name

def validateemployeename():
    while True:
        empname=input("Enter your Name:")
        if ' ' in empname:
            print('Sorry! The Name you entered has space. Please enter without space')
            continue
        elif (not(empname.isalpha())):
            print('Oops! Name should be in alphabets.Try again')
            continue
        elif len(empname)<=2:
            print('Sorry! The Name you entered is too short. Please enter a valid Name')
            continue
        elif empname in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":            
            print('Sorry! The Name you entered is invalid. Please enter a valid Name')
            continue               
        elif (not(empname.isalpha())):
           print('Oh no :( ! The Name you entered contains digit. Please enter a valid Name')
           continue
        elif findrepeated(empname):
            print('Sorry! The Name you entered has repeated alphabet. Please enter a valid Name')
            continue
        else:
            return empname

# Function to Validate Mobile Number

def validatemobileno():
    while True:
         mobno=input('Enter your Mobile Number:')        
         if (not(mobno.isdigit())):
            print('Oh-no! Mobile number should be in numeric.Give it an another try')
            continue
         elif len(mobno)!=10:
             print('Sorry! The Mobile Number you entered is below or above 10 digits. Please enter a valid Number')
             continue
         elif mobno.startswith(('0' , '1' , '2', '3', '4', '5')):
             print('Oops :( ! The Mobile Number you entered cannot start with 0 or 1 or 2 or 3 or 4 or 5. Please enter a valid Number')
             continue
         else:
             return mobno

# Function to Validate Email

def validateemail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True: 
        email=input('Enter email:')
        if(re.fullmatch(regex, email)):
            return email     
        else:
            print("Oops! Enter a valid email ID.Attempt again")
            continue

# Function to Validate DOB

def validatedob():
    while True:
            try:
                birthdate=input('Enter your DOB in the format YYYY-MM-DD:')
                dob= datetime.datetime.strptime(birthdate, '%Y-%m-%d')
                age=findage(dob)
                if age<0:
                    print("Oh-no! you have entered a future date")
                elif age in range(0,19):
                    print('You are too young. You have time to come again')
                elif age>60:
                    print("Thanks for your Splendid Service.Happy to bid you bye")
                else:
                    return age,birthdate
            except:
                    print("Oh-no! The date entered is invalid. Try again")
                    continue

# Function to Validate DOJ

def validatedoj():
    while True:
        try:
            joindate=input('Enter your DOJ in the format YYYY-MM-DD:')
            doj= datetime.datetime.strptime(joindate, '%Y-%m-%d')
            exp=findage(doj)
            if exp<0:
                print("Oops! you have entered a future date.Retry")
            else:
                return str(exp),joindate
        except:
            print("Sorry! The date entered is invalid. Try again")
            continue

# Function to Validate Qualification

def validatequalification():
    print("select your qualifiction:")
    print("Option 1 :  BTech Information Technology")
    print("Option 2 :  BE Computer Science")
    print("Option 3 :  BE Mechanical")
    print("Option 4 :  BE Automobile")
    print("Option 5 :  BE EEE")
    print("Option 6 :  BE ECE")
    print("Option 7 :  BTech BioMedical")
    print("Option 8 :  Others")
 
    while True:
        option=input("Select one of the options:")
        if not option.isdigit():
            print("Oops! You have entered a alphabet or special character . Choose a valid number between 1 and 8. Retry")
            continue
        elif int(option) not in range(1,9):
            print("Oops! choose a valid number between 1 and 8. Retry")
            continue
        else:
            qualification=switchqualification(int(option))
            break 
 
    if(qualification=='Others'):
        getqualification=input('Enter your qualification:')
        return getqualification
    else:
        return qualification

# Function to Validate Salary

def validatesalary():
    while True:
        salary=input('Enter your Salary:')    
        if (not(salary.isdigit())):
            print('Sorry :( ! Salary should be in numeric. Try Again')
            continue
        elif int(salary==0):
             print('Oh-no! salary should not be null. Retry')
             continue
        elif int(salary)<1000 or int(salary) >10000000:
            print("Sorry :( ! Salary range should be between 1000 and 1 crore. Re-attempt")
            continue
        else:
            return salary

# funtion for diplaying Employee credentials

def printinfo(eid,ename,eno,eemail,edob,edoj,equalify,esalary,eempdob,eempdoj):
    print("\nEMPLOYEE DETAILS\n")
    print('Employee ID      : '+eid)
    print('Employee Name    : '+ename)
    print('Mobile Number    : '+ eno)
    print('Email ID         : '+eemail)
    print('D.O.B            : '+eempdob)
    print("Age              : you are {} years and We are happy to have you here".format(edob))
    print('D.O.J            : '+eempdoj)
    print("Experience       : "+edoj+" years")
    print('Qualification    : '+equalify)
    print("Salary           : Rs."+esalary)

# Main funtion 

if __name__ == '__main__':
    distinctID=[]
    while True:
        print('\nWelcome to the Employee managament system.\nPlease enter your credentials\n')
        EMPLOYEEID=validateemployeeID(distinctID)
        EMPLOYEENAME=validateemployeename()
        EMPLOYEENUMBER=validatemobileno()
        EMPLOYEEEMAIL=validateemail()
        EMPLOYEEAGE,EMPDOB=validatedob()
        EMPLOYEEEXP,EMPDOJ=validatedoj()
        EMPLOYEEDOBQUALIFICATION=validatequalification()
        EMPLOYEESALARY=validatesalary()
        printinfo(EMPLOYEEID,EMPLOYEENAME, EMPLOYEENUMBER,EMPLOYEEEMAIL,EMPLOYEEAGE,EMPLOYEEEXP,EMPLOYEEDOBQUALIFICATION,EMPLOYEESALARY,EMPDOB,EMPDOJ)
        final=input('\nDo you you want to enter another employee record?(Y/N)')
        if final=='Y'or'y':
            continue
        else:
            print('\nThank You\n')
            break

# ************** END OF CODE ******************

 



             

            

