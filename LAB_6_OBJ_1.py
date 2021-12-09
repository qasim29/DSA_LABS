# OBJECT 1: Write a python program to check of the 
# given string is palindrome or not using stack.

class stack():
    def __init__(self):
        self.mylist = []
    def pop(self):
        return self.mylist.pop()
    def push(self,val):
        self.mylist.append(val)

a = input("Input a string: ")    
mystack=stack()
for i in a:
    mystack.push(i)
b=""
for i in a:
    b+=mystack.pop()
if (a==b):
    print("Its a palindrome string")
else:
    print("its not a palindrome string")







