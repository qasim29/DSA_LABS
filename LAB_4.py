
# list of integers
stack1 = [1,2,3,4,5,6,7,8,9,10]
# empty list
stack2 = []
# list with mixed data types
my_list1 = [1, "Hello", 3.4]
# nested list
my_list2 = ["mouse", [8, 4, 6], ['a']]
# list with characters
my_list3 = ['p', 'r', 'o', 'b', 'e']

# List indexing

print(my_list3[0])  # p

print(my_list3[2])  # o

print(my_list3[4]) # e

# Nested indexing
print(my_list2[0][1]) # o
print(my_list2[1][2]) # 6

# Negative indexing in lists
print(my_list3[-1]) #e
print(my_list3[-5]) #p

# Appending and Extending lists in Python
odd = [1, 3, 5]
odd.append(7)
print(odd)      #[1, 3, 5, 7]

# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)
print(odd)       #[1, 3, 9]

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list)  # Output: ['r', 'o', 'b', 'l', 'e', 'm']

# print count of 4
print(stack1.count(4))  #1

#reverse the list 
stack1.reverse()
print(stack1)       #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#copy the value in stack3
stack3 = stack1.copy()
print(stack3)      ##[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
