from Grade import grade
from Teacher import teacher

# Student
students = []

def addStudents():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        course = input('Enter Course: ')
        year = input('Enter year: ')
        section = input('Enter section: ')
        print('----------------------------')
        filipino = input('Grade filipino: ')
        math = input('Grade math: ')
        science = input('Grade science: ')
        english = input('Grade english: ')

        stud = grade(filipino, math, science, english)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

def deleteStudentRecord():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()


def searchStudentRecord():
    i = int(input('Enter index: '))
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')

    menu()


def displayStudentRecords():
    print()
    print('STUDENTS RECORD')
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()


# TEACHER
teachers = []

def addTeacher():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        Department = input('Enter Department: ')
        Position = input('Enter Position: ')

        teach = teacher(id, lastName, firstName, middleName, type, Department, Position)
        teach.id = id
        teach.last_name = lastName
        teach.first_name = firstName
        teach.middle_name = middleName
        teach.type = type

        teachers.append(teach)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

def deleteTeacherRecord():
    i = int(input('Enter index: '))
    teachers.pop(i)

    menu()


def searchTeacherRecord():
    i = int(input('Enter index: '))
    print(f'{i} \t {teachers[i].getName()} \t | {teachers[i].getDepartment()} \t | {teachers[i].getPosition()}')

    menu()


def displayTeacherRecords():
    print()
    print('TEACHER RECORD')
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

#DELETE AND DISPLAY ALL RECORDS
def displayAllRecord():
    print('-------------------------------------------------------------------------------')
    print('TEACHER RECORD')
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print()
    print('-------------------------------------------------------------------------------')
    print('STUDENT RECORD')
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def deleteAllRecords():
    teachers.clear()
    students.clear()

    menu()


def menu():
    print()
    print()
    print('::Menu::')
    print('D - delete student record        S - search student record')
    print('A - add student record           M - display student record')
    print('G - delete teacher record        F - search teacher record')
    print('C - add teacher record           N - display teacher record')
    print('X - display all record           Z - delete all record')
    print()

    choice = input('Enter a function: ')
    if (choice == 'D'):
        deleteStudentRecord()
    elif (choice == 'G'):
        deleteTeacherRecord()
    elif (choice == 'A'):
        addStudents()
    elif(choice == 'C'):
        addTeacher()
    elif (choice == 'S'):
        searchStudentRecord()
    elif (choice == 'F'):
        searchTeacherRecord()
    elif (choice == 'M'):
        displayStudentRecords()
    elif (choice == 'N'):
        displayTeacherRecords()
    elif (choice == 'X'):
        displayAllRecord()
    elif (choice == 'Z'):
        deleteAllRecords()
    print()

menu()
