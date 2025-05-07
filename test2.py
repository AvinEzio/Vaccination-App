

from json import load
from UserData import UserData, admin_login, sort_user_risk, sort_user_rsvp

# Creating UserData Object
database = UserData()

# Getting a specific user based on name
user = database.get_user("Marcus")

# Updating user password and store the changes.
user.password = "something new"
database.update_user()

sort_user_rsvp()

