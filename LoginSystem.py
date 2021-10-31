
import json
from UserData import UserData

filename = "users.json"

def options():
    print("1.View User Info")
    print("2.Update User Info")
    print("3.Quit")

def options2():
    print("1.Update User Info")
    print("2.Quit")

def signup():
    db = open("PasswordDatabase.txt","r")
    Username = input("Create Username: ")
    Password = input("Create Password: ")
    Password1 = input("Confirm Password: ")
    name =[]
    password = []
    for i in db:
        nm,pas = i.split(", ")
        pas = pas.strip()
        name.append(nm)
        password.append(pas)
    data = dict(zip(name, password))


    if Password != Password1:
        print("Passwords don't not match\nTry again")
        signup()
    else:
        if Username in name:
            print("This user already exists\nTry again")
            signup()
        else:
            db = open("PasswordDatabase.txt", "a")
            db.write("\n"+Username+", "+Password)
            print("Sign up successful\n")
            main_menu()

def access():
    db = open("PasswordDatabase.txt", "r")
    Username = input("Enter Username: ")
    Password = input("Enter Password: ")
    if not len(Username or Password) < 1:
        name =[]
        password = []
        for i in db:
            nm,pas = i.split(", ")
            pas = pas.strip()
            name.append(nm)
            password.append(pas)
        data = dict(zip(name, password))
        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login successful")
                        print("\n")
                        print("Welcome,",Username)
                        options()
                        x = int(input(">> "))
                        if x == 1:
                            database = UserData()
                            user = database.get_user(Username)
                            print("Name                            : " + user.name)
                            print("Phone Number                    : " + user.phone_number)
                            print("Occupation                      : " + user.occupation)
                            print("Vaccination                     : " + user.vaccination)
                            print("Covid-19 Status                 : " + user.covid_status)
                            print("Vaccine Status                  : " + user.vaccine_status)
                            print("Vaccination Appointment Date    : 1st Dose: " + user.vacc_apt_date1 + " | 2nd Dose: " + user.vacc_apt_date2)
                            print("Vaccination Appointment Location: " + user.vacc_apt_location)
                            print("\n\n")
                        if x == 2:
                            database = UserData()
                            user = database.get_user(Username)
                            user.phone_number = input("Enter your new phone number: ")
                            user.occupation = input("Enter your new job: ")
                            user.vaccination = input("Enter the number of vaccine doses recieved: ")
                            user.covid_status = input("Enter your COVID-19 status:  Positive | Negative\n>> ")
                            user.vaccine_status = ("")
                            user.vacc_apt_date1 = ("")
                            user.vacc_apt_date2 = ("")
                            user.vacc_apt_location = ("")
                            database.update_user()
                    else:
                        print("Incorrect username or password")
                except:
                    print("Incorrect username or password")
            else:
                print("User doesn't exist")
        except:
                print("User doesn't exist")


def main_menu(option = None):
    print("___Main Menu___")
    option = int(input("1.Login\n2.Sign Up\n>>"))
    if option == 1:
        access()
    elif option == 2:
        signup()
    else:
        print("Please enter a number to proceed")

main_menu() 
