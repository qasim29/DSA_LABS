import timeit

#Your statements here




class queue() :
    def __init__(self) :
        self.mylist = []
        self.rare = 0 
        self.front = 0
    def enqueue(self,val):
        if (self.rare <= 10):
            self.mylist.insert(self.rare,val)
            self.rare += 1
        else: 
            print("It is full")
    def dequeue(self):  
        val=None
        if (self.front <= 10 and self.rare>self.front):
            val = self.mylist[self.front]
            self.front+=1
        if (self.rare == self.front):
            print("Queue is reset nothing left to dequeue now.")
            self.front = 0
            self.rare = 0
        return val 
    def isEmpty(self):
        if (self.rare == 0 and self.front==0):
            print("its is empty")
            return True
        else:
            print("its is not empty") 
            return False
    def isFull(self):
        if (self.rare == 11 ):
            print("its is full")
            return True
        else:
            print("its is not full")
            return False
    def peek(self):
        if(not self.isEmpty()):
             print(self.front)
        else:
            print("Queue is empty")        
que = queue()
a = input("Enter String: ")

start = timeit.default_timer()
for i in a:
    que.enqueue(i)
b=0
for i in range(1,len(a)):
    if str(que.dequeue())==a[-i]:
        b=0
    else:
        b=1
        break
stop = timeit.default_timer()
if b==0:
    print("its a palindrome string")
else:
    print("its not a palindrome string")
print('Time: ', stop - start)



