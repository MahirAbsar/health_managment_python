# Health Management System

def getTime():
    import datetime
    return datetime.datetime.now()


# Writing
def logData():
    choice = int(input("HARRY - 1\nMARRY -2\nJERRY - 3\nFor Whom Do You Want to Log Data: "))
    if (choice == 1):
        choice_type = int(input("FOOD - 1\nEXCERCISE - 2\nFor What Do You Want to Log Data: "))
        if (choice_type == 1):
            f1 = open("harry_log_food.txt", "a")
            ask = input("Food: ")
            f1.write(str(getTime()) + " " + ask + "\n")
            f1.close()
        else:
            f1 = open("harry_log_excercise.txt", "a")
            ask = input("Excercise: ")
            f1.write(str(getTime()) + " " + ask + "\n")
            f1.close()
    elif (choice == 2):
        choice_type = int(input("FOOD - 1\nEXCERCISE - 2\nFor What Do You Want to Log Data: "))
        if (choice_type == 1):
            f2 = open("marry_log_food.txt", "a")
            ask = input("Food: ")
            f2.write(str(getTime()) + " " + ask + "\n")
            f2.close()
        else:
            f2 = open("marry_log_excercise.txt", "a")
            ask = input("Excercise: ")
            f2.write(str(getTime()) + " " + ask + "\n")
            f2.close()
    elif (choice == 3):
        choice_type = int(input("FOOD - 1\nEXCERCISE - 2\nFor What Do You Want to Log Data: "))
        if (choice_type == 1):
            f3 = open("jerry_log_food.txt", "a")
            ask = input("Food: ")
            f3.write(str(getTime()) + " " + ask + "\n")
            f3.close()
        else:
            f3 = open("jerry_log_excercise.txt", "a")
            ask = input("Excercise: ")
            f3.write(str(getTime()) + " " + ask + "\n")
            f3.close()


# Reading
def retrieve():
    choice = int(input("HARRY - 1\nMARRY -2\nJERRY - 3\nFor Whom Do You Want to Retrieve Data: "))
    if (choice == 1):
        choice_type = int(input("FOOD - 1\nEXCERCISE - 2\nFor What Do You Want to Log Data: "))
        if (choice_type == 1):
            try:
                f1 = open("harry_log_food.txt")
                print(f1.read())
                f1.close()
            except:
                print("No Information Logged Yet")
        else:
            try:
                f1 = open("harry_log_excercise.txt")
                print(f1.read())
                f1.close()
            except:
                print("No Information Logged Yet")
    elif (choice == 2):
        choice_type = int(input("FOOD - 1\nEXCERCISE - 2\nFor What Do You Want to Log Data: "))
        if (choice_type == 1):
            try:
                f2 = open("marry_log_food.txt")
                print(f2.read())
                f2.close()
            except:
                print("No Information Logged Yet")
        else:
            try:
                f2 = open("marry_log_excercise.txt")
                print(f2.read())
                f2.close()
            except:
                print("No Information Logged Yet")
    elif (choice == 3):
        choice_type = int(input("FOOD - 1\nEXCERCISE - 2\nFor What Do You Want to Log Data: "))
        if (choice_type == 1):
            try:
                f3 = open("jerry_log_food.txt")
                print(f3.read())
                f3.close()
            except:
                print("No Information Logged yet")
        else:
            try:
                f3 = open("jerry_log_excercise.txt")
                print(f3.read())
                f3.close()
            except:
                print("No Information Logged Yet")
    else:
        print("INVALID INPUT!!!!!")


logOrRetrieve = 0
person = 0
logOrRetrieve = int(input("Press 1 to log Data and 2 to retrieve Data: "))
if (logOrRetrieve == 1):
    logData()
else:
    retrieve()
