# I am using print() to have a newline of code
# EXERCISE LEVEL 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('Lenght of the set in IT companies is: ', len(it_companies))
print()
# add Twitter to the set
it_companies.add('Twitter')
print('Twitter is added to the IT companies: ', it_companies)
print()
# add 'Tesla', 'SpaceX', 'Alphabet' at oce
it_companies.update(['Tesla', 'SpaceX', 'Alphabet'])
print('New set of IT companies: ', it_companies)
print()
# removing Microsoft from the list
it_companies.remove('Microsoft')
print('Microsoft is removed from the list of IT companies: ', it_companies)
print()
# difference between remove and discard method
difference = '''The discard method is different from the remove () method,\nbecause the remove () method will raise an error if the specified item does not exist,\nand the discard () method will not.'''                  
print(difference)
print()

# EXERCISE LEVEL 2

# Join of set
Union = A.union(B)
print('Join of set A and B: ', Union)
print()

# intersection of set
ineter_section = A.intersection(B)
print('The intersection between Set A and Set B is: ', ineter_section)
print()
# subset of set
Sub_set = A.issubset(B)
print('Is A subset of B: ', Sub_set)
print()
# Disjoint of set
print('Are A and B disjoint sets: ', A.isdisjoint(B))
print()
# Join A with B and B with A
A_B = A.union(B)
B_A = B.union(A)
print('Join A with B: ', A_B)
print('Join B with A: ', B_A)
print()
# Symmetric difference of set
Symtrc_dffrnc = A.symmetric_difference(B)
print('The Symmetric difference between Set A and set B is: ', Symtrc_dffrnc)
print()
# Deleting of sets
del it_companies
del A
del B


# EXERCISE LEVEL 3
# converting of set
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print('The length of list age is: ', len(age))
print('The length of set age as set is: ', len(age_set))
print('Set comparison, set A is  greater than set B: ', len(age)>len(age_set))
print()
# differences between data types
diference_btwn_data_tp = 'Stirn is any character uyoucan write on the keyboard written as "strn64/j2", \nlist is a collection which is ordered and changeable(modifiable). Allows duplicate members, \nand Tuple is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members, \nwhile Set is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed'''
print(diference_btwn_data_tp)
print()
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print('the Unique words are: ', unique_words)
print('The number of unique words are: ', len(unique_words))

