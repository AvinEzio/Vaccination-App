# Vaccination-App
import json

user_info = '[{"user": "Alex","phone number": 01245675,"vaccination":"Yes"},\
            {"user": "John","pnone number": 0123456765,"vaccination":"No"},\
            {"user":"Mike","phone number": 01234445332,"vaccination":"Yes"},\
            {"user":"Marcus","phone number":0125673458,"vaccination":"No"}]'

open("user_info.json","w")
json.dumps(user_info)
