#create an empty list
my_list = []

#Append the elements to my list

my_list.extend(10, 20, 30, 40)
print(my_list)

#insert the value in second position 

my_list.insert([1],15)
print(my_list)

#extend my list with another list 
my_list.extend([50, 60, 70])
print(my_list)

#remove the last element
my_list.pop()

#sort the list in ascending order
my_list.sort()

#find value of 30
index_of_30 = my_list.index(30)
