keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict={}

for i in range(len(keys)):
    my_dict[keys[i]]=values[i]

print(my_dict)



family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price=0
for x,y in family.items():
    if y<3:
        print(f"{x} is free")
    elif y>=3 and y<=12:
        price=10+price
        print(f"{x} will cost 10$")
    else:
        price=15+price
        print(f"{x} will cost 15$")

print(price)



brand={"name":"zara","creation_date":1975, "creator_name":"Amancio Ortega Gaona",
        "types_of_clothes":['men', 'women', 'children', 'home'], "international_competitors":['gap', 'H&M', 'Benetton'],
        "number_of_stores": 7000,"major_color":{"france":"blue","spain":"red","US":['green','pink']}}


brand['number_of_stores']=2

print(f"zara has products for {brand["types_of_clothes"]}")
brand["country_of_creation"]="spain"

if "international_competitors" in brand:
    brand["international_competitors"].append('Desigual')

print(brand.items())
del brand["creation_date"]

print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])


print(len(brand))

for key in brand.keys():
    print(key)


users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict_1={}
dict_2={}
dict_3={}
sort_list=[]

for i in range(len(users)):
    dict_1[users[i]]=i

print(dict_1)

for i in range(len(users)):
    dict_2[i]=users[i]

print(dict_2)

sort_list=sorted(users)

for i in range(len(users)):
    dict_3[sort_list[i]]=i

print(dict_3)