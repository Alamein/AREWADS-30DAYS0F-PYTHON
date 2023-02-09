# I am using print() to have a newline in the next line code
# concanenate the string 'Thirty', 'Days', 'of', 'python'
a = 'Thirty'
b = ' Days'
c = ' Of'
d = ' Python'
full_str = a + b + c + d
print(full_str)
print()
cod = 'Coding'
fr = ' For'
al = ' All'
full_cd_str = cod + fr + al
print(full_cd_str)
print()
vrbl_for_nm = full_cd_str
print(vrbl_for_nm)
print(len(vrbl_for_nm))
print(vrbl_for_nm.upper())
print(vrbl_for_nm.lower())
print(vrbl_for_nm.capitalize(), vrbl_for_nm.title(), vrbl_for_nm.swapcase())
print(vrbl_for_nm[1:])
print(vrbl_for_nm.index('Coding'))
print(vrbl_for_nm.replace('Coding', 'Python'))
print()
# replacing python for everyone to python for all
pyth_fr_ev = 'Python For Everyone'
print(pyth_fr_ev, pyth_fr_ev.replace('Everyone', 'All'))
print()
# spliting the sentence coding for all
print(full_cd_str.split( ))
print()

# long string split
F,G,M,A,I,O,Am = 'Facecook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon'
full_com = F+G+M+A+I+O+Am
print(full_com.split( ))
print()
# showing the character on 0 in coding for all
print('The character at index 0 in the Coding For All is:', vrbl_for_nm[0])
print('The last index of the string Coding For All is: ', full_cd_str[-1])
print(full_cd_str.index(al))
print(full_cd_str[11])
print()
# abbreviation for pyhton for everyone and coding for all
print('Python For Everyone: PFE')
print('Coding For All: CFA')
print()
print(full_cd_str.index('C'))
print(full_cd_str.index('F'))
print()
# long sentence word indix
long_sntnc = '''You cannot end a sentence with because because because is a conjunction'''
print(long_sntnc.index('because'))
print(long_sntnc.rindex('because'))
print(long_sntnc[31:55])
print()
# checking startswith
print('Does CFA starts with Coding: ', vrbl_for_nm.startswith('Coding'))
print('Does CFA ends with Coding: ', vrbl_for_nm.endswith('Coding'))
print()
rmv = '   Coding For All      '
print(rmv[3:17])
dift1 = '30DaysOfPython'
dift2 = 'thirty_days_of_python'
print('30DaysOfPython is identifier: ', dift1.isidentifier())
print('thirty_days_of_python is identifier: ', dift2.isidentifier())
print()
# Libraries
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result_of_libry = '# '.join(libraries)
print(result_of_libry)
print()
# newline escape system
newline_escape = 'I am enjoying this challenge. \nI just wonder what is next.'
print(newline_escape)
print()
# string format system
radius = 10
area = 3.14 * radius ** 2
print('The area of a cycle with radius {} is {} meters square.'.format(radius, area))
print()
a = 14
ab = 2
abb = 48
abbb = 1.33
abbbb = 2
abbbbb = 1
abbbbbb = 262144
print('Python basics mathematics operations\n8 + 6 = {}\n8 - 6 = {}\n8 * 6 = {}\n8 / 6 = {}\n 8 % 6 = {}\n8 // 6 = {}\n8 **6 = {}'.format(a, ab, abb, abbb, abbbb, abbbbb, abbbbbb))
