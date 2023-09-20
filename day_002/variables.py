# I am using print() to have a newline in the next line code
# Day 2: 30 Days of Python Programming
# exercise level 1
first_name = 'Aminu'
last_name = 'Nababa'
full_name = 'Aminu Hamza Nababa'
country = 'Nigeria'
city = 'Kano'
age = int(19)
year = int(2023)
is_married = False
is_true = 'Yes'
is_light_on = 'Yes'
student, techie, passionate_about_it, arewa_data_science_fellow, arewa_data_sciene_mentor = True, True, 'Yes', True, False
print('First name: ', first_name)
print('Last name: ', last_name)
print('Full name: ', full_name)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Year: ', year)
print('Is married: ', is_married)
print('Is true: ', is_true)
print('Is light on: ', is_light_on)
print('Is he student: ', student)
print('Is he Techie: ', techie)
print('Is Al\'amin passionate about Arewa data science academy: ', passionate_about_it)
print('Is Al\'amin fellow of Arewa data science academy: ', arewa_data_science_fellow)
print('Is Al\'amin mentor of Arewa data science academy: ', arewa_data_sciene_mentor)

# exercise level 2
print() # I use this print() command to get line space between code
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(student))
print(type(techie))
print(type(passionate_about_it))
print(type(arewa_data_science_fellow))
print(type(arewa_data_sciene_mentor))
print()
print(len(first_name))
print(len(first_name)-len(last_name))
print()
num_one = int(5)
num_two = int(4)
total = num_one + num_two
diff = num_one - num_two
product = num_two*num_one
division = num_one/num_two
remainder = num_one%num_two
exp = num_one**num_two
floor_division = num_one//num_two
print(num_one)
print(num_two)
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)
print()

# calculation of circle
area_of_circle = float(format(3.142*(30**2), '.2f'))
circum_of_cicle = float(format(2*3.142*30, '.2f'))
print('The Are of circle with radius 30 is: ', area_of_circle)
print('The circumference of cicle with r = 30 is: ', circum_of_cicle)
area_of_cicle_from_user = int(input('Write the radius of cicle: '))
Area_of_user = float(format(3.142*(area_of_cicle_from_user**2), '.2f'))
print('The Area of the cicle is: ', Area_of_user)
print()

# user info
user_first_name = input('Write your first name: ')
user_last_name = input('Write your last name: ')
user_Country = input('write your Country name: ')
user_age = int(input('Write your age: '))
print('Your first name is: ', user_first_name)
print('Your last name is: ', user_last_name)
print('Your country is: ', user_Country)
print('Your age is: ', user_age)
