# I am using print() for new line in the output of the code
# EXERCISE LEVEL 1
# exercise 1
import random
import string
x = string.ascii_letters + string.digits
lst = []
lst[:0] = x

def random_user_id():
    y=' '
    for i in range(6):
        y+=random.choice(lst)
    return y
print(random_user_id())
print()

# exercise 2
def user_id_gen_by_user():
    y = int(input('Enter the number of characters in user ID: '))
    x = int(input('Enter the number of user  ID to be generated: '))
    for i in range(x):
        z = ' '.join([random.choice(lst) for i in range(y)])
        print(z)
    return ' '
print(user_id_gen_by_user())
print()

# exercise 
def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"
print(rgb_color_gen())
print()

# EXERCISE LEVEL 2
# exercise 1
def list_of_hexa_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    hexas = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    hexCodes = []
    for _ in range(many):
        hexCodes.append("#" + ''.join([random.choice(hexas) for _ in range(6)]))
    return hexCodes
print(list_of_hexa_colors(many=0))
print()

# exercise 2
def list_of_rgb_colors(many=0):
   def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b =str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"
    if many == 0:
        many = random.randint(1, 10)
    rgbs = []
    for _ in range(many):
        rgbs.append(rgb_color_gen())
    return rgbs
print(list_of_rgb_colors(many=0))
print()

# exercise 3
def generate_colors(col_type,many):
    if col_type == 'hexa':
        return list_of_hexa_colors(many)
    elif col_type == 'rgb':
        return list_of_rgb_colors(many)
    else:
        return "Invalid Input"
print(generate_colors("hexa",0))
print()

# EXERCISE LEVEL 3
# exercise 1
import random
def shuffled_list(array):
    return random.sample(array, len(array))
print(shuffled_list([0,5,6,6]))
print()
# indeed python is awesome I Aminu Hamza Nababa I am so much enjoying 30 days of python.
# execise 2
def seven_random():
    arr = []
    length = -1
    while length <= 7:
        num = random.randint(0, 9)
        if num not in arr:
            arr.append(num)
            length = len(arr)
    return arr
print(seven_random())
print()
