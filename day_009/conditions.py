# I am using print() to have a newline of code
# EXERCISE LEVEL 1
# exercise num1
user_age = int(input('Enter your age and see if you can drive: '))
if user_age >= 18:
    print('You are old enough to drive.')
else:
    years_remain = 18 - user_age
    print('You need', years_remain, 'more years to start driving.')
print()

# exercise num2
my_age = 19
user_age = int(input('Enter your age: '))
if my_age == user_age:
    print('We have the same years.')
elif my_age < user_age:
    age_difference = user_age - my_age
    if age_difference == 1:
        print('You are 1 year older than me.')
    else:
        print('You are', age_difference, 'years older than me.')
else:
    age_difference = my_age - user_age
    if age_difference == 1:
        print('I am 1 year older than you.')
    else:
        print('I am', age_difference, 'years older than you.')
print()

# exercise num3 
num_a = int(input('Wirte a any number: '))
num_b = int(input('Write any number gain: '))
if num_a > num_b:
    print(num_a, 'is greater than', num_b)
elif num_a < num_b:
    print(num_a, 'is smaller than', num_b)
else:
    print(num_a, 'is equal to', num_b)
print()

# EXERCISE LEVEL 2
# exercise num1
score = int(input('Enter your score: '))
if score >= 80 and score <= 100:
    print('Your Grade score is A')
elif score >= 70 and score <= 89:
    print('Your Grade score is B')
elif score >= 60 and score <= 69:
    print('Your Grade score is C')
elif score >= 50 and score <= 59:
    print('Your Grade score is D')
else:
    print('Your Grade score is F')
print()

# exercise num2
month = input('Enter the name of a month to see your existine season: ')
if month in ['September', 'October', 'November']:
    print('The season is Autumn')
elif month in ['December', 'January', 'February']:
    print('The season is Winter')
elif month in ['March', 'April', 'May']:
    print('The season is Spring')
elif month in ['June', 'July', 'August']:
    print('The season Summer')
print()
# exercise num3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Write the name of a fruit: ')
if fruit in fruits:
    print('The fruit is already exist in the list of our fruits')
else:
    fruits.append(fruit)
    print('The modified list of fruits: ', fruits)
print()

# EXERCISE LEVEL 3

my_info = {
    'first_name': 'Aminu',
    'last_name': 'Nababa',
    'age': 19,
    'country': 'Nigeria',
    'is_married': False,
    'skills': ['HTML', 'CSS', 'Mathematics', 'Python', 'Physics'],
    'address': {
        'street': 'Premier Hospital',
        'zipcode': '700103'
    }
}

if 'skills' in my_info:
    skills = my_info['skills']
    middle_skill = skills[len(skills) // 2]
    print("The middle skill:", middle_skill)


if 'skills' in my_info:
    if 'Python' in my_info['skills']:
        print('The person has the Python skill')
    else:
        print('The person does not have the Python skill')
print()

if 'skills' in my_info:
    skills = my_info['skills']
    if skills == ['JavaScript', 'React']:
        print('He is a front end developer')
    elif skills == ['Node', 'Python', 'MongoDB']:
        print('He is a backend developer')
    elif skills == ['React', 'Node', 'MongoDB']:
        print('He is a fullstack developer')
    else:
        print('unknown title')
print()
if my_info['is_married'] and my_info['country'] == 'Nigeria':
    print(f"{my_info['first_name']} {my_info['last_name']} is married and lives in {my_info['country']}")
