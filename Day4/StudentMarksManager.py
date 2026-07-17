# Simple Student Marks Manager

students = []
math = []
sci = []
eng = []
total = []
average = []


def add_st():
    while True:
        name = input("Enter student name: ")

        students.append(name)

        m = int(input("Enter Math marks: "))
        s = int(input("Enter Science marks: "))
        e = int(input("Enter English marks: "))

        math.append(m)
        sci.append(s)
        eng.append(e)

        t = m + s + e
        total.append(t)
        average.append(t / 3)

        more = input("Do you want to add another student? (yes/no): ").lower()

        if more != "yes":
            break


while True:

    choice = int(input("""
1. Add Student
2. Delete Student
3. Show Student Marks
4. Show All Students
5. Update Student Marks
6. Show Student Average
7. Show Student Total
8. Search Student
9. Exit

Enter your choice: """))

    if choice == 1:
        add_st()

    elif choice == 2:
        name = input("Enter student name to delete: ")

        if name in students:
            i = students.index(name)

            students.pop(i)
            math.pop(i)
            sci.pop(i)
            eng.pop(i)
            total.pop(i)
            average.pop(i)

            print("Student deleted successfully.")

        else:
            print("Student not found.")

    elif choice == 3:
        name = input("Enter student name: ")

        if name in students:
            i = students.index(name)

            print("Student:", students[i])
            print("Math:", math[i])
            print("Science:", sci[i])
            print("English:", eng[i])

        else:
            print("Student not found.")

    elif choice == 4:

        if len(students) == 0:
            print("No students found.")

        else:
            for i in range(len(students)):
                print("---------------------")
                print("Student:", students[i])
                print("Math:", math[i])
                print("Science:", sci[i])
                print("English:", eng[i])
                print("Total:", total[i])
                print("Average:", average[i])

    elif choice == 5:
        name = input("Enter student name: ")

        if name in students:
            i = students.index(name)

            math[i] = int(input("Enter Math marks: "))
            sci[i] = int(input("Enter Science marks: "))
            eng[i] = int(input("Enter English marks: "))

            total[i] = math[i] + sci[i] + eng[i]
            average[i] = total[i] / 3

            print("Marks updated successfully.")

        else:
            print("Student not found.")

    elif choice == 6:
        name = input("Enter student name: ")

        if name in students:
            i = students.index(name)
            print("Average:", average[i])

        else:
            print("Student not found.")

    elif choice == 7:
        name = input("Enter student name: ")

        if name in students:
            i = students.index(name)
            print("Total:", total[i])

        else:
            print("Student not found.")

    elif choice == 8:
        name = input("Enter student name: ")

        if name in students:
            i = students.index(name)

            print("Student Found")
            print("Math:", math[i])
            print("Science:", sci[i])
            print("English:", eng[i])
            print("Total:", total[i])
            print("Average:", average[i])

        else:
            print("Student not found.")

    elif choice == 9:
        print("Thank you for using the program.")
        break

    else:
        print("Invalid choice.")