import json

my_family = {
    "parents" :['Beth', 'Jerry'],
    "children" :['Summer', 'Morty']
}

json_my_family = json.dumps(my_family)
print(json_my_family)