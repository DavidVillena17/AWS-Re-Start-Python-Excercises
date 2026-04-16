"""
Script: collectionss.py
Descripción: Trabajo con estructuras de datos nativas de Python (Listas, Tuplas y Diccionarios).
"""
my_fruit_list = ["apple", "banana", "cherry"]
print(my_fruit_list)
print(type(my_fruit_list))

print(my_fruit_list[0])
print(my_fruit_list[1])
print(my_fruit_list[2])

my_fruit_list[2] = "orange"
print(my_fruit_list)

my_final_answer_tuple = ("apple", "banana", "pineapple")
print(my_final_answer_tuple)
print(type(my_final_answer_tuple))

print(my_final_answer_tuple[0])
print(my_final_answer_tuple[1])
print(my_final_answer_tuple[2])


my_favorite_fruit_dictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(my_favorite_fruit_dictionary)
print(type(my_favorite_fruit_dictionary))

print(my_favorite_fruit_dictionary["Akua"])
print(my_favorite_fruit_dictionary["Saanvi"])
print(my_favorite_fruit_dictionary["Paulo"])


#Lab
my_mixed_type_list = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in my_mixed_type_list:
    print("{} is of the data type {}".format(item,type(item)))