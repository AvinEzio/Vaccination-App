
from User import User
import json

filename = "user.json"

class UserData(object):
  def __init__(self):
    self.users = load_user()

# This method will get user object based on name
  def get_user(self, name):
      for user in self.users:
        if(user.name == name):
          return user
        else:
          raise "User not found"

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
      print("Loading : " + user.name)
  return users


