# EXERCISE LEVEL1
# I am using print() to have newline to the next code
# execise num 1
empty_tuple = ()
print('This is empty turple: ', empty_tuple)
print()
# execise num2
sisters_tuple = ('Shahidat', 'Hafsat', 'Fatima', 'Bara atu', 'Baby', 'Afnan')
brothers_tuple = ('Muddassir', 'Sabir')
# execise num3
sibilings_tuple = brothers_tuple + sisters_tuple
# execise num4
print('I have ', len(sibilings_tuple), ' siblings')
# execise num5
modify_siblngs_tuple = list(sibilings_tuple)
print('Here are my siblings: ', modify_siblngs_tuple)
print()
family_members = ['Hamza', 'Sadiya' ] + modify_siblngs_tuple
print('Here are my family members', family_members, ' including me')
print()

# EXERCISE LEVEL2
# execise num1
family_members = ['Hamza', 'Sadiya' ] + modify_siblngs_tuple
*father,sblng1,sblng2,sblng3sblng4,sblng5,sblng,sblng7,sblng8 = family_members
print('Unpack tuple: ', *father,sblng1,sblng2,sblng3sblng4,sblng5,sblng,sblng7,sblng8)
print()
# execise num2
fruits = ('Lemon', 'water melon', 'Banana', 'Apple')
vegetables = ('Carrot', 'Lattuse', 'Tomato')
animal = ('Duck', 'Hen', 'Ram')
food_stuff_tp = fruits + vegetables + animal
print('Tuple joining sample: ', food_stuff_tp)
print()
# execise num3
food_stuff_lt = list(food_stuff_tp)
print()
# execise num4
print(food_stuff_tp[4:6])
print()
# execise num5
print(food_stuff_lt[0:4])
print(food_stuff_lt[7:10])
# execise num6
# since food stuff it is the samething as food stuff tp 
food_stuff_lt = list(food_stuff_tp)
del food_stuff_lt
# execise num7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
check_if_a = 'Estonia' in nordic_countries
check_if_b = 'Iceland' in nordic_countries
print('Estonia is in nordic countries: ', check_if_a)
print('Iceland is in nordic countries: ', check_if_b)



