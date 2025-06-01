"""Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]"""
my_set = {1,5,9,10}
print(my_set)
my_set_2 = {2.5,6.7,0.9,5.7}
print(my_set_2)
my_set_3 = {-1,2,3,4,3,24}
print(my_set_3)
my_set_4 = {1,2,3,2}
print(my_set_4)
my_set_5= {0,1,3,4,5}
my_set_5.pop()
print(my_set_5)