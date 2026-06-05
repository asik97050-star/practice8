students = []

while True:
    print("\n1 - Студент қосу")
    print("2 - Студенттер тізімі")
    print("3 - Студент іздеу")
    print("4 - Шығу")

    choice = input("Таңдаңыз: ")

    if choice == "1":
        name = input("Студент аты: ")
        students.append(name)
        print("Студент қосылды!")

    elif choice == "2":
        print("\nСтуденттер тізімі:")
        for student in students:
            print(student)

    elif choice == "3":
        search = input("Ізделетін студент аты: ")
        if search in students:
            print("Студент табылды!")
        else:
            print("Студент табылмады!")

    elif choice == "4":
        print("Бағдарлама аяқталды.")
        break

    else:
        print("Қате таңдау!")