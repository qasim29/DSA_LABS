



# a = int(input("Enter the number: "))
# b=1
# for i in range(1,a+1):
#     b=b*i
# print("Factorial is: ", b)

# b=int(input("Enter Ihe Number: "))

# def fact(b):
#     if(b==1):
#       return b
#     else:
#         return b*fact(b-1)
# print("the factorial is: ",fact(b))


# class Click_Counter:

#   def __init__(self) :
#     self.count=0
#     self.countDisplay()
    
#   def pushBtn(self):
#     self.count+=1
#     self.countDisplay()

#   def resetBtn(self):
#     self.count=0
#     self.countDisplay()

#   def countDisplay(self):
#     print("The count is: ",self.count)


def main():
  a = Click_Counter()
  
  print("TO increcement Count press : 1\nTO reset Count press : 2"
  "\nTo display count press: 3\nTO Exit the Program press: 4\n")
  
  while(True):
    b=int(input("Enter your choice: "))
    if(b==1):
      a.pushBtn()
    elif (b==2):
      a.resetBtn()
    elif(b==3):
      a.countDisplay()
    elif(b==4):
      print("bye !!!")
      break
    else: print("please choose the correct option")


# main()





    