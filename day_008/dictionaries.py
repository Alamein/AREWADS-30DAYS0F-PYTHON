# I am using print() to have a newline of code
# Exercise num1
dog_dictnr = {}

# Exercise num2
dog_dictnr['name'] = 'Police Dog'
dog_dictnr['color'] = 'White'
dog_dictnr['breed'] = 'German'
dog_dictnr['legs'] = 4
dog_dictnr['age'] = 2
print('My Dog Dictionary: ', dog_dictnr)
print()
# Exercise num3
student_dictnr = {}
student_dictnr['first_name'] = "Al'amin"
student_dictnr['last_name'] = 'Nababa'
student_dictnr['gender'] = 'Male'
student_dictnr['age'] = 19
student_dictnr['marital_status'] = 'Single'
student_dictnr['skills'] = ['HTML', 'CSS', 'Js', 'Python',]
student_dictnr['country'] = 'Nigeria'
student_dictnr['city'] = 'Abuja'
student_dictnr['address'] = 'Sreet 4 Nuber.433 Garki Abuja'
print('Student Dictionary: ', student_dictnr)
print()
# Exercise num4
print("Length of Student Dictionary:", len(student_dictnr))
print()
# Exercise num5
skills = student_dictnr['skills']
print('Student Skills: ', skills)
print("Data type of skills:", type(skills))
print()
# Exercise num6
student_dictnr['skills'].extend(['Data Science'])
print('Modified student Skills: ', student_dictnr['skills'])
print()
# Exercise num7
keys = list(student_dictnr.keys())
print("Dictionary Keys:", keys)
print()
# Exercise num8
values = list(student_dictnr.values())
print("Dictionary Values:", values)
print()
# Exercise num9
items = list(student_dictnr.items())
print('Tuple: ', items)
print()
# Exercise num10
del student_dictnr['address']
print("Dictionary after deletion:", student_dictnr)
print()
# Exercise num11
del student_dictnr
