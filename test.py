msg = "Hellpo World"
print(msg)

#Data Types
#There is no explicit data type declaration is required

pi = 22 / 7
var1 = 2999

#The ideal value of pi is 3.141...
print(f"The value of pi without typecase is {pi}")
#When type casted the value of the pi to intefer
print(f'The value of pi type casted to integer is {int(pi)}')
#The value of integer variable when type casted to float
print(f'The value of integer value when converted to float is {float(var1)}')


#Strings
#There are lot of string functions in python a few of them are 
#Capitalize the first letter in a sentence
print('dArWin'.capitalize)
#Replace function
print('eragon'.replace('e', 'd'))
#Split a list of values with a delimiter
print("ID|Name|Address|Contact".split('|'))


#Boolean and None
# If there is a value in a variable then it is True, here the truth value is True / False. 
# #The first letter is uppercase

py_fundas = True
ux_fundas = False

print(f"The truth value of the py_fundas is {py_fundas} in numeric form is  {int(py_fundas)}")
print(f"The truth value of the ux_fundas is {ux_fundas} in numeric form is {int(ux_fundas)}")

#If condition

if var1 == 2999:
    print("The number matched with the variable value")
else:
    print("The number did not match")

#Lists and Loops
student_names = ["Mark", "Katrina", "Jessica", "Randy"]
# The index can start from 0 left to right
print(f'First item in list is {student_names[0]}')
# The index can start from -1 right to left
print(f'Last item in the list is {student_names[-1]}')
# If an invalid index is given, will get an exception.

# How many elements in the list
print(f'number of items in list is {len(student_names)}')




#Break and Continue
#While Loops 
#Dictionaries
#Exceptions
#Other Data Types
