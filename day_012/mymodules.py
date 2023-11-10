def generate_fullname(firstname, lastname):
    fullname = firstname + " " + lastname
    return fullname


def addition(num1, num2):
    total = num1 + num2
    return f'The summation of the given numbers is {total}'


def weight_of_object(mass, acceleration):
    weight = format(mass*acceleration, '.0f')
    return weight
print('The weight of object is: ', weight_of_object(100, 9.8), 'N', sep='')


