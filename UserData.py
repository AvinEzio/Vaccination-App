from User import User
import json

filename = "users.json"

class UserData(object):
    def __init__(self):
        self.users = load_user()

# This method will get user object based on name
    def get_user(self, name):
        for user in self.users:
            if(user.name == name):
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
    with open("users.json", "r") as f:
        gobble = json.loads(f.read())
        return gobble



def sort_user():
    info = user()
    userRisk = sorted(info, key = lambda k: k["covid_status"], reverse= True)
    userRisk = userRisk[:5]
    print("High risk: 1 | Low risk: 0")
    for i in userRisk:
        print("{name} : {covid_status}".format(**i))

