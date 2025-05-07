
from User import User
import json


filename = "users.json"

class UserData(object):
    def __init__(self):
        self.users = load_user()

# This method will get user object based on name
    def get_user(self, Ic_no):
        for user in self.users:
            if(user.Ic_no == Ic_no):
                return user
        raise "Error"
    
    def get_user_Ic(self, Ic_no):
        for user in self.users:
            if(user.Ic_no == Ic_no):
                return user
        raise "Error"

    def get_user_status(self, vaccine_status):
        for user in self.users:
            if(user.vaccine_status == vaccine_status):
                return user
        raise "Error"

# This method will update json file with latest data
    def update_user(self):
        with open(filename,"w") as info:
            json.dump(self.users, info, indent = 4, default=encode_user)

# This is use to convert User Class to json.    
def encode_user(obj):
    if isinstance(obj, User):
        return obj.__dict__
    return obj

# This method will load user from json file
def load_user():
    with open(filename, "r") as data:
        jsonData = json.load(data)
        users = [User(**k) for k in jsonData]
        for user in users:
            print("")
    return users



def user():
    with open("users.json", "r") as info:
        data = json.loads(info.read())
        return data

def sort_user_risk():
    info = user()
    userRisk = sorted(info, key = lambda k: k["med_history"], reverse= True)
    userRisk = userRisk[:]
    print("High risk | Low risk\nHigh Risk Users: Yes | Low Risk Users: No\n#*********************************************************************************\n")
    for i in userRisk:
        print("Name: {name} | IC No: {Ic_no}\nPhone Number: {phone_number}\nUser Risk: {med_history}\n".format(**i))

def sort_user_rsvp():
    info = user()
    userRsvp = sorted(info, key = lambda k: k["rsvp"], reverse= True)
    userRsvp = userRsvp[:]
    print("RSVP : Yes | No\n#*********************************************************************************\n")
    for i in userRsvp:
        print("Name: {name} | IC No: {Ic_no}\nVaccination RSVP: {rsvp}\n".format(**i))

def sort_user_status():
    info = user()
    userStatus = sorted(info, key = lambda k: k["vaccine_status"], reverse= True)
    userStatus = userStatus[:]
    print("Assigned | Not Assiged\n#*********************************************************************************\n")
    for i in userStatus:
        print("Name                            : {name}\nIC Number                       : {Ic_no}\nAge                             : {age}\nPriority                        : {pr}\nPhone Number                    : {phone_number}\nVaccination Appointment         : {vaccine_status}\nVaccination RSVP                : {rsvp}\nVaccination                     : {vaccination}\nCovid-19 Status                 : {covid_status}\nVaccination Time                : {vacc_time}\nVaccination Appointment Date    : 1st Dose: {vacc_apt_date1} | 2nd Dose: {vacc_apt_date2}\nVaccination Appointment Location: {vacc_apt_location}\n\n".format(**i))


def view_users():
    print("View All Users\n#*********************************************************************************\n")
    with open(filename,"r") as info:
        users = json.load(info)
        for access in users:
            Ic = access["Ic_no"]
            name = access["name"]
            age = access["age"]
            phone_num = access["phone_number"]
            add_ = access["add"]
            job = access["occupation"]
            vaccine = access["vaccination"]
            covid = access["covid_status"]
            vaccine_status = access["vaccine_status"]
            rsvp = access["rsvp"]
            time = access["vacc_time"]
            vaccine_date1 = access["vacc_apt_date1"]
            vaccine_date2 = access["vacc_apt_date2"]
            vaccine_location = access["vacc_apt_location"]
            print(f'IC Number                       : {Ic}')
            print(f'Name                            : {name}')
            print(f'Phone Number                    : {phone_num}')
            print(f'Address                         : {add_}')
            print(f'Occupation                      : {job}')
            print(f'Vaccination                     : {vaccine}')
            print(f'Covid-19 Status                 : {covid}')
            print(f'Vaccine Status                  : {vaccine_status}')
            print(f'Vaccination RSVP                : {rsvp}')
            print(f'Vaccination Time                : {time}')
            print(f'Vaccination Appointment Date    : 1st Dose: {vaccine_date1} | 2nd Dose: {vaccine_date2}')
            print(f'Vaccination Appointment Location: {vaccine_location}')
            print("\n\n")

def admin_update():
    database = UserData()
    user = database.get_user_Ic(input("Enter the IC Number Of The User You Want To Update\n>> "))
    print("IC Number                       : " + user.Ic_no)
    print("Name                            : " + user.name)
    print("Age                             : " + user.age)
    print("Priority                        : " + user.pr)
    print("Phone Number                    : " + user.phone_number)
    print("Address                         : " + user.add)
    print("Occupation                      : " + user.occupation)
    print("Vaccination                     : " + user.vaccination)
    print("Covid-19 Status                 : " + user.covid_status)
    print("Vaccine Status                  : " + user.vaccine_status)
    print("RSVP Vaccination                : " + user.rsvp)
    print("Vaccination Time                : " + user.vacc_time)
    print("Vaccination Appointment Date    : 1st Dose: " + user.vacc_apt_date1 + " | 2nd Dose: " + user.vacc_apt_date2)
    print("Vaccination Appointment Location: " + user.vacc_apt_location)
    print("\n")
    print("__Admin Update Options__")
    print("1.Update Vaccination Appointment")
    print("2.Number of Vaccine Dosses")
    print("3.COVID-19 Status")
    print("4.Vaccination Status")
    print("5.Vaccination Dose Date")
    print("6.Vaccination Location")
    print("7.Update Vaccination Time")
    print("8.Catogarize User Priority")
    print("9.Update All")
    print("10.Back")
    x = int(input(">> "))
    if x == 1:
        user.vacc_time = input("Enter Vaccination Time\n>> ")
        print("Enter A Vaccination Date: Day/Month/Year | XX/XX/XXXX")
        user.vacc_apt_date1 = input("Enter 1st Vaccination Dose Date\n>> ")
        user.vacc_apt_date2 = input("Enter 2nd Vaccination Dose Date\n>> ")
        user.vacc_apt_location = input("Enter Vaccination Location\n>> ")
    elif x == 2:
        user.vaccination = input("Enter the number of vaccine doses recieved: 1 Dose | 2 Dose\n>> ")
    elif x == 3:
        user.covid_status = input("Enter Your COVID-19 Status: Positive | Negative\n-> (Under Quarantine / Normal)\n\n>> ")
    elif x == 4:
        user.vaccine_status = input("Vaccination Status: Assigned | Not Assigned\n>> ")
    elif x == 5:
        print("Enter A Vaccination Date: Day/Month/Year | XX/XX/XXXX")
        user.vacc_apt_date1 = input("Enter 1st Vaccination Dose Date\n>> ")
        user.vacc_apt_date2 = input("Enter 2nd Vaccination Dose Date\n>> ")
    elif x == 6:
        user.vacc_apt_location = input("Enter Vaccination Location\n>> ")
    elif x == 7:
        user.vacc_time = input("Enter Vaccination Time\n>> ")
    elif x == 8:
        user.pr = input("Enter A Number To Catogarize User Priority: 1-5\n>> ")
    elif x == 9:
        user.vaccination = input("Enter the number of vaccine doses recieved\n>> ")
        user.covid_status = input("Enter Your COVID-19 Status: Positive | Negative\n-> (Under Quarantine / Normal)\n\n>> ")
        user.vaccine_status = input("Vaccination Status: Assigned | Not Assigned\n>> ")
        user.vacc_time = input("Enter Vaccination Time\n>> ")
        user.vacc_apt_date1 = input("Enter 1st Vaccination Dose Date\n>> ")
        user.vacc_apt_date2 = input("Enter 2nd Vaccination Dose Date\n>> ")
        user.vacc_apt_location = input("Enter Vaccination Location\n>> ")
        user.pr = input("Enter A Number To Catogarize User Priority: 1 - 5\nHighest Priority = 1 |Least Priority = 5\n>> ")
    elif x == 10:
        print("")
    database.update_user()



