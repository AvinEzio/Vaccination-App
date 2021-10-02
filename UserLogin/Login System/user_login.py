import json
from os import access, read
def login():
    with open("user.json","r") as x:
        user = json.load(x)
        for access in user:
            username = access["name"]
            password = access["phone number"]

def entry():
    with open("user.json","r") as x:
        for access in x:
            username = ["name"]
            password = ["phone number"]

def menu():
    print("1.Login\n2.Sign Up\n3.Quit")



while True:
    menu()
    user_input = input("Enter A Number To Proceed: ")
    if user_input == "1":
        login()
        if input("Enter Username: ") and input("Enter Password; ") == "Alex" and 1234:
            print("Login Successful")
        else:
            print("login fail")
            break
    elif user_input == "2" or "3":
        break

#*******************************************


