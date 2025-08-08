import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}\star_wars.txt', 'r', encoding='utf-8') as f:
 txt_list= f.readlines()
 for line in txt_list:
     print(line)
print ("end of document")

print(txt_list[4])

print(txt_list[0][:4])


temp=[list(line) for line in txt_list]
print(temp)


counts={"Darth":0,"Luke":0,"Lea":0}
for line in txt_list:
    line=line.strip()
    if line == "Darth":
        counts["Darth"] += 1
    elif line == "Luke":
        counts["Luke"] += 1
    elif line == "Lea": 
        counts["Lea"] += 1
print(counts)

modified_line=[]
for line in txt_list:
    if line.strip() =="Luke":
        modified_line.append("Luke skywalker\n")
    else:
        modified_line.append(line)

with open(f'{dir_path}\star_wars.txt', 'w', encoding='utf-8') as f:
    f.seek(0)
    f.writelines(modified_line)