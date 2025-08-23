import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data=json.loads(sampleJson)
print(data["company"]["employee"]["payable"]["salary"])
data["company"]["employee"]["birth_date"]="2000-06-08"
with open("modified_data.json", "w") as file:
    json.dump(data, file, indent=4)

