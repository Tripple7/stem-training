#List comprehension
my_list=[2,4,3,5,7,6,8]
other_list=[]
for x in my_list:
    other_list.append(x)
print(other_list)


my_list=[2,4,3,5,7,6,8]
other_list=[x for x in my_list]
print(other_list)

my_list=[2,4,3,5,7,6,8]
other_list=[]
for x in my_list:
    if x % 2 ==0:
        other_list.append(x)
print(other_list)

my_list=[2,4,3,5,7,6,8]
other_list=[x for x in my_list if x % 2==0]
print(other_list)

def add(a,b):
    return a+b
result= add(4,6)
print(result)

result_2=add(8,6)
print(result_2)

