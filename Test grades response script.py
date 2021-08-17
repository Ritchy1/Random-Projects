testscores = [0, 0, 0, 0, 0]


def response():
    resp = input("")

    if resp == "1":
        first_option()
    elif resp == "2":
        second_option()
    elif resp == "3":
        third_option()
    else:
        start()


def first_option():
    total = 0
    for i in range(5):
        total += testscores[i]
    print("Here is your average test score:", total / 5)
    print("")
    dialogue()


def second_option():
    print("Here are your test results -")
    print("")
    for i in range(5):
        if testscores[i] >= 90:
            print(testscores[i], "- Good job! You received a: A")
        elif testscores[i] >= 80:
            print(testscores[i], "- You're almost there! You received a: B")
        elif testscores[i] >= 70:
            print(testscores[i], "- Study more! You received a: C")
        elif testscores[i] >= 60:
            print(testscores[i], "- Tsk tsk....go to office hours! You received a: D")
        else:
            print(testscores[i], "- no beuno :( you received a: F")
    print("")
    dialogue()


def third_option():
    total = 0
    for i in range(5):
        total += testscores[i]
    print("Here is your average test score:", total / 5)
    print("")
    second_option()


def dialogue():
    print("What information would you like to gather?:")
    print("- Type 1: to receive the average of all five of your test scores.")
    print("- Type 2: to receive a letter grade for all five tests.")
    print("- Type 3: to receive the average and letter grade for all five of your tests.")
    print("- Type: any other number to re-enter test scores.")
    print("Enter number below -")

    response()


def start():
    print("please enter 5 test scores.")
    for i in range(5):
        testscores[i] = float(input("Enter test score here: "))
    print("")

    dialogue()


def main():
    start()


main()
