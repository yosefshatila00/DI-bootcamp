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
