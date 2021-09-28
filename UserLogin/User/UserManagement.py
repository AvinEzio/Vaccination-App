from UserData import UserData

# Creating UserData Object
database = UserData()

# Getting a specific user based on name
user = database.get_user("Alex")
print("current password" + user.password)

# Updating user password and store the changes.
user.password = "something new"
database.update_user()
