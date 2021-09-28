# Vaccination-App
import json

#Creating Preset Users
user_info = '[{"user": "Alex","phone number": 01245675,"vaccination":"Yes"},\
            {"user": "John","phone number": 0123456765,"vaccination":"No"},\
            {"user":"Mike","phone number": 01234445332,"vaccination":"Yes"},\
            {"user":"Marcus","phone number":0125673458,"vaccination":"No"}]'
            
#Load To A JSON File
with open("user_info.json","w") as info:
json.dumps(user_info,info)
