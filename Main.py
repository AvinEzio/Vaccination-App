import json
from Options import admin_options, main_options, med_history_options, update_user_options
from UserData import UserData, admin_update, sort_user_risk, sort_user_rsvp, sort_user_status, view_users

filename = "users.json"


def signup():
    db = open("PasswordDatabase.txt","r")
    Ic_no = input("Enter Your IC Number: ")
    Password = input("Create Password: ")
    Password1 = input("Confirm Password: ")
    Ic =[]
    password = []
    for i in db:
        ic,pas = i.split(", ")
        pas = pas.strip()
        Ic.append(ic)
        password.append(pas)
    if Password != Password1:
        print("Passwords don't not match\nTry again")
        signup()
    else:
        if Ic_no in Ic:
            print("This user already exists\nTry again")
            signup()
        else:
            db = open("PasswordDatabase.txt", "a")
            db.write("\n"+Ic_no+", "+Password)
            name = input("Enter Your Name: ")
            print("Sign up successful\n")
    db = open("PasswordDatabase.txt", "r")
    user_data = {}
    with open (filename,'r') as info:
        users = json.load(info)
        user_data["Ic_no"] = (Ic_no)
        user_data["name"] = (name)
        user_data["age"] = ("")
        user_data["password"] = (Password)
        user_data["phone_number"] = ("")
        user_data["add"] = ("")
        user_data["pc"] = ("")
        user_data["occupation"] = ("")
        user_data["vaccination"] = ("")
        user_data["covid_status"] = ("")
        user_data["vaccine_status"] = ("")
        user_data["rsvp"] = ("")
        user_data["vacc_time"] = ("")
        user_data["vacc_apt_date1"] = ("")
        user_data["vacc_apt_date2"] = ("")
        user_data["vacc_apt_location"] = ("")
        users.append(user_data)
        with open(filename,"w") as info:
            json.dump(users, info, indent = 4)
    main_menu()

def userssssssss():
    with open("users.json", "r") as info:
        data = json.loads(info.read())
        return data

def access():
    db = open("PasswordDatabase.txt", "r")
    Ic_no = input("Enter Your IC Number: ")
    Password = input("Enter Password: ")
    if not len(Ic_no or Password) < 1:
        Ic =[]
        password = []
        for i in db:
            ic,pas = i.split(", ")
            pas = pas.strip()
            Ic.append(ic)
            password.append(pas)
        data = dict(zip(Ic, password))
        try:
            if data[Ic_no]:
                try:
                    if Password == data[Ic_no]:
                        database = UserData()
                        user = database.get_user(Ic_no)
                        print("\nLogin successful\n\nWelcome, " + user.name+ "\n")
                        x = 11
                        while x != 10:
                            main_options()
                            x = int(input(">> "))
                            print("\n")
                            if x == 1:
                                database = UserData()
                                user = database.get_user(Ic_no)
                                print("IC Number                       : " + user.Ic_no)
                                print("Name                            : " + user.name)
                                print("Age                             : " + user.age)
                                print("Phone Number                    : " + user.phone_number)
                                print("Address                         : " + user.add)
                                print("Postal Code                     : " + user.pc)
                                print("Occupation                      : " + user.occupation)
                                print("Vaccination                     : " + user.vaccination)
                                print("Covid-19 Status                 : " + user.covid_status)
                                print("\n")
                            elif x == 2:
                                update_user_options()
                                database = UserData()
                                user = database.get_user(Ic_no)
                                y = int(input(">> "))
                                print("\n")
                                if y == 1:
                                    user.name = input("Enter Your Name: ")
                                    user.age = input("Enter Your Age: ")
                                    user.phone_number = input("Enter your new phone number: ")
                                    database.update_user()
                                elif y == 2:
                                    user.occupation = input("Enter your new occupation: ")
                                    database.update_user()
                                elif y == 3:
                                    med_history_options()
                                    z = input("Yes | No\n>> ")
                                    d = z.lower()
                                    print("")
                                    if d == "yes":
                                        user.med_history = ("High")
                                    elif d == "no":
                                        user.med_history = ("Low")
                                    database.update_user()
                                elif y == 4:
                                    user.covid_status = input("Enter Your COVID-19 Status: Positive | Negative\n-> (Under Quarantine / Normal)\n\n>> ")
                                    print("")
                                    database.update_user()
                                elif y == 5:
                                    user.add = input("Enter Your Address: ")
                                    user.pc = input("Enter Your Postal Code: ")
                                elif y == 6:
                                    user.name = input("Enter Your Name: ")
                                    user.age = input("Enter Your Age: ")
                                    user.phone_number = input("Enter your new phone number: ")
                                    user.add = input("Enter Your Address: ")
                                    user.pc = input("Enter Your Postal Code: ")
                                    user.occupation = input("Enter your new job: ")
                                    med_history_options()
                                    z = input("Yes | No\n>> ")
                                    d = z.lower()
                                    print("")
                                    if d == "yes":
                                        user.med_history = ("High")
                                    elif d == "no":
                                        user.med_history = ("Low")
                                    database.update_user()
                                elif y == 7:
                                    print("")
                            elif x == 3:
                                database = UserData()
                                user = database.get_user(Ic_no)
                                print("Vaccine Status                  : " + user.vaccine_status)
                                print("RSVP Vaccination                : " + user.rsvp)
                                print("#*********************************************************************************\n")
                                print("IC Number                       : " + user.Ic_no)
                                print("Name                            : " + user.name)
                                print("Vaccination                     : " + user.vaccination)
                                print("Covid-19 Status                 : " + user.covid_status)
                                print("Vaccination Time                : " + user.vacc_time)
                                print("Vaccination Appointment Date    : 1st Dose: " + user.vacc_apt_date1 + " | 2nd Dose: " + user.vacc_apt_date2)
                                print("Vaccination Appointment Location: " + user.vacc_apt_location)
                                print("\n")
                            elif x == 4:
                                database = UserData()
                                user = database.get_user(Ic_no)
                                print("Vaccination                     : " + user.vaccination)
                                print("Covid-19 Status                 : " + user.covid_status)
                                print("Vaccine Status                  : " + user.vaccine_status)
                                print("RSVP Vaccination                : " + user.rsvp)
                                print("Vaccination Time                : " + user.vacc_time)
                                print("Vaccination Appointment Date    : 1st Dose: " + user.vacc_apt_date1 + " | 2nd Dose: " + user.vacc_apt_date2)
                                print("Vaccination Appointment Location: " + user.vacc_apt_location)
                                print("\n")
                                user.rsvp = input("RSVP your vaccination appointment: Yes | No\n>> ")
                            elif x == 5:
                                main_menu()
                            database.update_user()
                    else:
                        print("\nIncorrect IC Number or Password\n")
                        main_menu()
                except:
                    print("\nIncorrect IC Number or Password\n")
                    main_menu()
            else:
                print("\nThis User Doesn't Exsist\n")
                print("1.Try Logging In Again")
                print("2.Sign Up")
                x = int(input(">> "))
                if x == 1:
                    access()
                elif x == 2:
                    signup()
        except:
                print("\nThis User Doesn't Exsist\n")
                print("1.Try Logging In Again")
                print("2.Sign Up")
                x = int(input(">> "))
                if x == 1:
                    access()
                elif x == 2:
                    signup()

def admin_login():
    db = open("AdminPassword.txt", "r")
    Admin_name = input("Enter your Username: ")
    Password = input("Enetr your password: ")
    if not len(Admin_name or Password) < 1:
        name = []
        password = []
        for i in db:
            nm,pas = i.split(", ")
            pas = pas.strip()
            name.append(nm)
            password.append(pas)
        data = dict(zip(name, password))
        try: 
            if data[Admin_name]:
                try:
                    if Password == data[Admin_name]:
                        print(f"\nAdmin Login successful\nWelcome, {Admin_name}\n")
                        x = 11
                        while x != 10:
                            admin_options()
                            x = int(input(">> "))
                            print("\n")
                            if x == 1:
                                view_users()
                                print("\n")
                            elif x == 2:
                                admin_update()
                                print("\n")
                            elif x == 3:
                                database = UserData()
                                user = database.get_user_Ic(input("Enter the IC Number Of The User You Want To Assign An Appointment\n>> "))
                                user.vaccine_status = ("Assigned")
                                user.vacc_time = input("Enter Vaccination Time\n>> ")
                                user.vacc_apt_date1 = input("Enter 1st Vaccination Dose Date\n>> ")
                                user.vacc_apt_date2 = input("Enter 2nd Vaccination Dose Date\n>> ")
                                user.vacc_apt_location = input("Enter Vaccination Location\n>> ")
                                print("\n")
                                database.update_user()
                            elif x == 4:
                                sort_user_rsvp()
                                print("\n")
                            elif x == 5:
                                sort_user_status()
                                print("\n")
                            elif x == 6:
                                sort_user_risk()
                                print("\n")
                            elif x == 7:
                                main_menu()
                    else:
                        print("\nIncorrect username or password\n")
                        main_menu()
                except:
                    print("\nIncorrect username or password\n")
                    main_menu()
            else:
                print("\nAdmin doesn't exist\n")
                main_menu()
        except:
                print("\nAdmin doesn't exist\n")
                main_menu()


def main_menu(option = None):
    print("___Main Menu___")
    option = int(input("1.Login\n2.Sign Up\n3.Admin Login\n>> "))
    if option == 1:
        access()
    elif option == 2:
        signup()
    elif option == 3:
        admin_login()
    else:
        print("Please enter a number to proceed")
        main_menu()


main_menu()
