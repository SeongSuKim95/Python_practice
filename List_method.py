#Append
num = [1,2,3,4]
num.append(5)
print(num) # [1,2,3,4,5]

#Extend
#list.extend(iterable)

num1 = [5,6]
num2 = [7,8]

num1.extend(num2)

print(num1) #[5,6,7,8]

#Insert

char = ['a','b','c','d']

char.insert(3,'e')
print(char)# ['a','b','c','e','d']

mixed_list = [{1,2},[5,6,7]]

num_tuple = (3,4)

mixed_list.insert(1,num_tuple)

print(mixed_list)

#Remove
#Only removes the first matching element
num.remove(1)
print(num)

#Count
for i in range(10):
    num.append(1)

print(num)
count = num.count(1)
print(count)
count = mixed_list.count((3,4))
print(count)

#Pop
#Remove and return n th item

pop = num.pop(1)
print(pop,num)

for i in range(13):
    pop = num.pop(-1)
    #pop from end
    print(pop,num)

#Reverse
## list.reverse() = list[::-1]
Os = ['windows','macOS','Linux']
Os.reverse()
print(Os)
print(Os[::-1])

for item in reversed(Os):
    print(item)

#Sort
#list.sort(key=...,reverse=...)
#sorted(list,key=...,reverse=...)
#sort() method doesn't return any value. Rather, it changes the original list.

num3 = [3,1,2,3,4,5]
num3.sort()
print(num3)
num3.sort(reverse=True)
print(num3)

def takeSecond(elem):
    return elem[1]

random = [(2,2),(3,4),(4,1),(1,3)]
random.sort(key=takeSecond)

print(random)

##Dictionary Sorting
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

num4 =[1,2,3,4,5]
new_num4 = num4.copy()
print(new_num4)

num4.clear()
print(num4)

num5 =[1,2,3,4,5]
del num5[:]
print(num5)