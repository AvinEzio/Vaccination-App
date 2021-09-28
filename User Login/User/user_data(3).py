import json

users = [json]

data = users
data = {}
data ['user']= []
data['user'].append({
    'name': 'Alex',
    'phone number': '0125839577',
    'vaccination': "Yes"
})

with open("user.json","w") as user_data:
    user_data.dump(json)
