# Exercise Level 2

# 1
# command for checking the python version: python --version
print('python version : 3.10.0 64-bit')
print()
# 2
print(3 + 4)      # Addition(+)
print(4 - 3)      # Subtraction(-)
print(3 * 4)      # Multiplication(*)
print(4 / 3)      # Division(/)
print(3 ** 4)     # Exponential(**)
print(4 % 3)      # Reminder(%)
print(4 // 3)     # Floor division operator(//)
print()
# 3
print("AMINU HAMZA NABABA")
print("Alhaji Nababa")
print("Nigeria")
print("I am enjoying 30 Days of python")
print()
# 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('AMINU HAMZA NABABA'))
print(type('Alhaji Nababa'))
print(type('Nigeria'))
print()
# Exercise level 3
print('Intiger : ...-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7...')
print()
print('Float : 1.01, 2.33, 2.5, 5.7777, 1.333')
print()
print('Complex : 2 + 2i, 4 + 4j, 3 * 2i')
print()
print("String: "
"'Aminu' "
"\n'Nababa' "
"\n'Python' "
"\n'I love python' "
"\n'I am enjoying 30 days of python' ",)

print()
print('Boolean: True False')
print()
print("List: ", [0, 1, 2, 3, 4, 5],['Banana', 'Orange', 'Lemon', 'Mango'], ['Corea','Cameroon', 'Niger','Ghana'], ['Battery', 30, False, 7.11])
print()
print("Turple: ",('John', 'Joserph', 'Thomson', 'Earnest', 'Rutherford')) # Names)
print()
print("Set: ", {4, 7, 1, 9},
{5.34, 6.98, 2.7}) #set of numbers)
print()
print("Dictionary: ", {
'first_name':'\nAminu',
'last_name':'Nababa',
'country':'Nigeria', 
'age':19, 
'is_married': False,
'skills':['HTML', 'CSS', 'Mathematics', 'Python']
})
print()
# Python Euclidian Distance

point_1 = (2,3)
point_2 = (10,8)

def naive_euclidian_distance(point1, point2):
    return sum([(point1[x] - point2[x]) ** 2 for x in range(len(point1))]) ** 0.5

print(naive_euclidian_distance(point_1, point_2))
