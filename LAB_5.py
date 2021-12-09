# // . OBJECT 4: Implement a function with signature transfer(S, T) that transfers all ele ments from stack S
# //             onto stack T, so that the element that starts at the top of S is the first to be inserted onto T, and the element at
# //             the bottom of S ends up at the top of T.

# from typing import List


# stack1 = [1,2,3,4,5,6,7,8,9,10]
# # empty list
# stack2 = []

# def transfer(s1,s2):
#     for i in range(len(s1)):
#         s2.append(s1.pop())

# print("stack before swap")
# for i in stack1:
#     print(i)

# print("stack after swap")
# transfer(stack1,stack2)

# for i in stack2:
#     print(i)


    
class stack():
    def __init__(self):
        self.list=[]
    def pop(self):
        self.list.pop()
        print(self.list)
    def push(self,a):
        self.list.append(a)
        print(self.list)
    def isEmpty(self):
        if (len(self.list)):
            return False
        else: return True
    def top(self):
        return self.list[-1]
    def len(self):
        return len(self.list)
    def transfer(self,list2):
        for i in range(len(self.list)):
            list2.append(self.list.pop())
        self.list = list2.copy()
        return self.list

def main():
  a = stack()
  print("\nTo Push in stack press: 1\nTo Pop from stack press: 2"
        "\nTO Check if empty press: 3\nTo get the top press: 4"
        "\nTo get the length press: 5\nTo Transfer stack press: 6"
        "\nTo Exit press: 6")
  while(True):
    b=int(input("Enter your choice: "))
    if(b==1):
        c=int(input("Enter the number: "))
        a.push(c)
    elif (b==2):
        a.pop()
    elif(b==3):
        print("Stack is empty: ",a.isEmpty())
    elif(b==4):
        print("The Top is: ",a.top())
    elif(b==5):
        print("The length is: ",a.len())
    elif(b==6):
        list2=[]
        print(a.transfer(list2))
    elif(b==7):
      print("bye !!!")
      break
    else: print("please choose the correct option")    

main()
