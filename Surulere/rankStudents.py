# Read the names and marks of at least 3 students
# Rank the top three students with highest marks
# Give cash rewards. $500 for first rank, $300 for second rank, $100 for third rank. Value cannot be modified
# Appreciate students who secured 950 marks and above

import operator
import random

print("Create an account".upper())
print()
print('To Proceed With Creation Of Account, Type "Create" Or "create"')
Account = input()

if(Account == 'Create' or Account == 'create'):
    firstName = input("Firstname:",)
    Username1 = input("Username:",)
    Password1 = int(input("Password:",))

number = random.randint(1,1001)

print("signed up successfully")
print()
print("Welcome to student grading system".upper())
print()
print("Log in".upper())
loop = "true"
while(loop == 'true'):
    Username = input("Username:",)
    Password = int(input("Password:",))
    if(Username1 == Username and Password1 == Password):
        print("Logged in successfully as_" + Username)
        loop = 'fasle'
        loop1 = 'true'
        while(loop1 == 'true'):
            print('To continue this program type "continue or Continue"')
            command = input(Username + "() > > ")
            if(command == 'continue' or command == 'Continue'):
                break
            else:
                print("'" + command + "' is not valid command!")
    else:
        print("Invalid Credential")



def readStudentDetails():
    print()
    # { 'John': 600, 'Ben': 800, 'David': 950, 'Mark': 980}
    print("Enter the number of students: ")
    numberOfStudents = int(input())
    studentRecord = {}
    for student in range(0, numberOfStudents):
        print("Enter the name of the student: ")
        name = input()
        print("Enter the marks of students: ")
        marks = int(input())
        studentRecord[name] = marks
    print()
    return studentRecord


def rankStudents(studentRecord):
    try:
        print()
        # [('Mark', 980), ('David', 950), ('Ben', 800), ('John', 600)]
        sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
        print(sortedStudentRecord)
        print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        print()
        return sortedStudentRecord
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()


def rewardStudents(sortedStudentRecord, reward):
    print()
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
    print()


def appreciateStudents(sortedStudentRecord):
    print()
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:
            break
    print()

    print("Project Develop by: \n Rotimi, Abdul Basit Olanrewaju".upper())

studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)
