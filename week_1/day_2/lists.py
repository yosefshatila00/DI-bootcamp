list1=[5, 10, 15,20, 25, 50,20]
if 20 in list1:
    index1=list1.index(20)
    list1[index1]=200

print(list1)


a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple
print(a)
print(b)
print(c)
print(d)

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

print(a_dict.items())

for key, value in a_dict.items():
    print(key, '->', value)