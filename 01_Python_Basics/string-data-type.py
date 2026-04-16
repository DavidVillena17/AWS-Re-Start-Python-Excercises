"""
Descripción: Uso y manipulación de variables de tipo cadena de texto (strings). 
"""
my_string = "This is a string."
print(my_string)
print(type(my_string))
print(my_string + " is of the data type " + str(type(my_string)))


first_string = "water"
second_string = "fall"
third_string = first_string + second_string
print(third_string)


name = input("What is your name? ")
print(name)


color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
print(f"{name} your favorite color is \n {color}")














