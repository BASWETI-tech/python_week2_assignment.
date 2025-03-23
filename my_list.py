#creating an empty list
my_list = []
print(my_list) 
#appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#inserting 15 in index 1
my_list.insert(1,15)
print(my_list)
#extending to the list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list)
#removing the last element from my list
my_list.pop(-1)
print(my_list)
#sorting my list in asceding order
my_list.sort()
print(my_list)
#indexing
index_of_30 = my_list.index(30)
print(f"index of 30: {index_of_30}")
