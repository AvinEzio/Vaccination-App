
import json

info = {}
info['user'] = []
info['user'].append({
    'name': 'Alex',
    'phone number' : '0122969357',
    'vaccination': 'Yes'
})

info['user'].append({
    'name': 'John',
    'phone number': '0125839577',
    'vaccination': 'No'
})

info['user'].append({
    'name': 'Mike',
    'phone number': '0122390605',
    'vaccination': 'Yes'
})

info['user'].append({
    'name': 'Marcus',
    'phone number': '0122842801',
    'vaccination': 'No'
})

with open('json.txt', 'w') as data:
    json.dumps(info, data)
    info.write(info)

