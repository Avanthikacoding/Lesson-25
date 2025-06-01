"""Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}"""
my_set_1 = {"green","blue" , "red" , "pink"}
my_set_2 = {"blue" , "red" , "yellow" , " purple"}
my_set_3 = my_set_1.intersection(my_set_2)
print(my_set_3)
my_set_4 = my_set_1.union(my_set_2)
print(my_set_4)
my_set_5 = my_set_1.difference(my_set_2)
print(my_set_5)
my_set_6 = my_set_1.symmetric_difference(my_set_2)
print(my_set_6)
