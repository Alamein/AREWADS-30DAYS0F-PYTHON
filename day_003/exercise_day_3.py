# I am using print() to have a newline in the next line code instead of \n

# age height and complex number info
age = int(19)
height = float(6.5)
complex_number = complex(2 + 8j)
print('The Age is: ', age, 'yers old')
print('The height is: ', height, 'm', sep='')
print('The stored complex number is: ', complex_number)
print()

# area of triangle
print('Do you want to find the area of triangle? \nwrite its base and height magnitude below')
base = float(input('write the base magnitude  of the triangle: '))
height_of_triangle = float(input('write the height magnitude  of the triangle: '))
area_of_triangle = float(format(0.5*base*height_of_triangle, '.2f'))
print('The area of triangle is: ', area_of_triangle, 'cm', sep='')
print()

# perimeter of triangle
print('Do you want to find the perimeter of triangle? \nwrite its base, leangth and height magnitude below')
side_a = float(input('write the leangh magnitude of the triangle: '))
side_b = float(input('write the base magnitude  of the triangle: '))
side_c = float(input('write the height magnitude  of the triangle: '))
perimeter_of_triangle = float(format(side_a+side_b+side_c , '.2f'))
print('The perimeter of the triangle is: ', perimeter_of_triangle, 'cm', sep='')
print()

# area of rectangle
print('Do you want to find the area of rectangle? \nwrite its leangth and width magnitude below')
length_0f_rectangle = float(input('Write the length magnitude of rectangle: '))
width_of_rectangle = float(input('Write the length magnitude of rectangle: '))
area_of_rectangle = float(format(length_0f_rectangle*width_of_rectangle, '.2f'))
print('The area of the rectangle is: ', area_of_rectangle)
print()

# perimeter of rectangle
print('Do you want to find the perimeter of rectangle? \nwrite its width, leangth magnitude below')
length_0f_rectangle = float(input('Write the length magnitude of rectangle: '))
width_of_rectangle = float(input('Write the length magnitude of rectangle: '))
perimeter_of_rectangle = float(format(2*(length_0f_rectangle+width_of_rectangle), '.2f'))
print('The perimeter of the rectangle is: ', perimeter_of_rectangle, 'cm', sep='')
print()

# getting the area of a circle
print('To calculate the area of a cicle, write the magnitude of its radius below')
radius_of_circle = float(input('write the magnitude of the radius of cicle: '))
pi = float(3.142)
area_of_circle = float(format(pi*(radius_of_circle*radius_of_circle), '.2f'))
print('The area of the circle is: ', area_of_circle)
print()

# getting the circumference of a circle
print('To calculate the circumference of a cicle, write the magnitude of its radius below')
radius_of_circle = float(input('write the magnitude of the radius of cicle: '))
pi = float(3.142)
circum_of_circle = float(format(2*(pi*radius_of_circle), '.2f'))
print('The circumference of the circle is: ', circum_of_circle, 'cm', sep='')
print()

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# The point are point1=(2,2) point2=(3,4)
change_in_y = int(4-2)
change_in_x = int(3-2)
slope = float(format(change_in_y/change_in_x, '.2f'))
print('The slope in x-intercept and y-intercept of y = 2x -2 is: ', slope, 'cm', sep='')
print()

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# To find Euclidean we must import "math"
change_in_y_b = int(10 - 2)
change_in_x_b = int(6 - 2)
slope_b = float(format(change_in_y_b/change_in_x_b, '.2f'))
print('The slope in x-intercept and y-intercept of y = 2x -2 is equal to slope \nwith point1(2,2) and point2(6,10): ', slope==slope_b)
# Euclidean Distance
import math
Ecldn_dstnc = math.sqrt((change_in_x_b)**2 + (change_in_y_b)**2)
print('\nThe Euclidean distance is: ', Ecldn_dstnc, 'cm', sep='')

# Calculate the value of y (y = x^2 + 6x + 9)
value_of_y = int(((-3)**2) + (6*(-3)) + 9)
print('if x is -3 in the equation x^2 + 6x + 9, then the value of y is: ',value_of_y)
print()

# finding the len of python and dragon and making falsy statement
python_len = len('python')
dragon_len = len('dragon')
print('The len of python is greater than len of dragon: ', python_len > dragon_len)
print()

# checking word 'on' in python and dragon
print('The word on can be found in both \'python\' and \'dragon\': ', 'on' in 'dragon' and 'Python')
print()
sentence = 'I hope this course is not full of jargon'
print('I hope this course is not full of jargon: ', 'jargon' in sentence)
print()
print("There is no 'on' in both 'dragon' and 'python': ", 'on' not in 'dragon and python')
print()
python_len = len('python')
python_len_f = float(len('python'))
python_len_str = str(len('python'))
print(python_len,python_len_f,python_len_str)
print()

# how to check data type
print('We can check the even numbers by using \'/\' division sign if its even it will leave no remainder')
print()
print('7/3 is equal to the converted value int 2.7: ', 7/3 == 2.7) # false
print()
print("'10' is equal to 10 in python: ", '10' == 10) # false
print()
print("int('9.8')is equal to 10: ", int(9.8) == 10)  # false
print()

# accepting data from the user to calculate his rate pay per hour
rate_per_hour = float(input('Enter rate per hour: '))
hour = float(input('Enter hours: '))
earning = float(format(rate_per_hour*hour, '.2f'))
print('Your weekly earning is: ','$', earning, sep='')

# calculating number of second of the user years
year_user = int(input('How old are you? '))
seconds_c = float(format(year_user*365*24*60*60, '.2f'))
print('You have lived for ', seconds_c,'seconds',sep='')

# the table of numbers
table = '\n1 1 1 1 1 \n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125'
print('The table of numbers: ', table)