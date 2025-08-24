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

# Step 1: Load the JSON string
data = json.loads(sampleJson)

# Step 2: Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

# Step 3: Add the "birth_date" key to the employee dictionary
data["company"]["employee"]["birth_date"] = "1990-05-15"

# Step 4: Save the JSON to a file
with open("modified_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Modified JSON has been saved to 'modified_data.json'")