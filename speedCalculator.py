from time import *
import random as r


def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error


def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput) / time_r
    return round(speed)


while True:
    chk = input("Ready to test : yes/no : ")
    if chk == "yes":
        test = ["this is a time speed calculator", "it is a python based project",
                "we can calculate our typing speed using this calculator"]
        test1 = r.choice(test)
        print("***** typing speed *****")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter : ")
        time_2 = time()

        print('Speed : ', speed_time(time_1, time_2, testinput), "w/sec")
        print("Erorr : ", mistake(test1, testinput))
    elif chk == "no":
        print("Thank you")
        break
    else:
        print("Wrong information")
