# create an empty list
my_list = []

#append elements in the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert the value 15 at the second positon in the list
my_list.insert(1, 15)

# extend the list with the values [50,60,70]
my_list.extend([50,60,70])

# remove the last from my_list
my_list.pop()

# sort the my_list in ascending order
my_list.sort()

# find and print the index of the value 30 in my_list
print(my_list.index(30))