from time import *
import random as r

def mistake(partest, usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error+=1
        except:
            error+=1
    return error
def speed_time(time_st,time_en, userinput):
    time_delay= time_en - time_st
    time_R= round(time_delay,2)
    speed= len(userinput)/time_R
    return round(speed)
while True:
    ck=input("Are you Ready?? yes/no: ")
    if ck=="yes":

        test=["The national animal of India is Tiger", "The national bird of India is Peacock", "What is the ratio of width of our national flag to its length?", "National Vegetable of India is Pumpkin"]
        test1=r.choice(test)
        print("************ Typing speed checker ******************")
        print(test1)
        print()
        print()
        time1=time()
        testinput=input("Enter: ")
        time2= time()

        print('Speed:', speed_time(time1, time2, testinput),"w/sec")
        print("Error: ", mistake(test1, testinput))
    elif ck=="no":
        print("Thank You!! See You Again")
        break
    else:
        print("You Pressed something Wrong..Sorry for the inconvenience, Test again!")

