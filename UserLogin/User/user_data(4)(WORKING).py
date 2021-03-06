import json 
filename = "user.json"

def options():
    print("Admin Data Management System")
    print("(1) View User Info")
    print("(2) Update User Info")
    print("(3) Quit")

def view_user_info():
    with open(filename, "r") as info:
        users = json.load(info)
        for access in users:
            name = access["name"]
            phone_num = access["phone_number"]
            job = access["occupation"]
            vaccine = access["vaccination"]
            covid = access["covid_status"]
            vaccine_status = access["vaccine_status"]
            vaccine_date1 = access["vacc_apt_date1"]
            vaccine_date2 = access["vacc_apt_date2"]
            vaccine_location = access["vacc_apt_location"]
            print(f'Name                            : {name}')
            print(f'Phone Number                    : {phone_num}')
            print(f'Occupation                      : {job}')
            print(f'Vaccination                     : {vaccine}')
            print(f'Covid-19 Status                 : {covid}')
            print(f'Vaccine Status                  : {vaccine_status}')
            print(f'Vaccination Appointment Date    : 1st Dose: {vaccine_date1} | 2nd Dose: {vaccine_date2}')
            print(f'Vaccination Appointment Location: {vaccine_location}')
            print('\n\n')

def update_data():
    user_data = {}
    with open (filename,'r') as info:
        users = json.load(info)
    user_data["name"] = input("Name: ")
    user_data["password"] = input("Enter Password: ")
    user_data["phone_number"] = input("Phone Number: ")
    user_data["occupation"] = input("Occupation: ")
    print("Vaccination Status | Done(1 Dose/2 Dose/None)")
    user_data["vaccination"] = input(": ")
    print("COVID-19 Test | Enter (Positive/Negative)")
    user_data["covid_status"] = input(": ")
    print("If Vaccinated Enter 'Assigned' If NOt Vaccinated, Enter 'Not Assigned'")
    user_data["vaccine_status"] = input(": ")
    print("If Vaccinated, Enter Vaccination Date(day/month/year) or 'None' If Not Vaccinated")
    user_data["vacc_apt_date1"] = input("1st Dose: ")
    user_data["vacc_apt_date2"] = input("2nd Dose: ")
    print("Enter Your Vaccination Location or 'None' If Not Vaccinated")
    user_data["vacc_apt_location"] = input(": ")
    users.append(user_data)
    with open(filename,"w") as info:
        json.dump(users, info, indent = 4)

while True:
    options()
    option  = input("Enter A Number: ")
    if option == "1":
        view_user_info()
    elif option == "2":
        update_data()
    elif option == "3":
        break
    else:
        print("Please Select A Number.")


