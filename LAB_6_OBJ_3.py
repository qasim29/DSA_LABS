# OBJECT 3:
# Write a program that takes two positive integers (say M, N) as inputs.
# It should first enqueue N random integers one by one into a queue, and then dequeue
# the N elements.
# This process should be repeated M times.
# Use the following in turn to store the queue:
# (a) a usual Python list, and
# (b) the alternative implementation suggested above, and compare the times
# taken by the two implementations.

import timeit
import random
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
            self.front = 0
            self.rare = 0
            return val
        return val 
    def isEmpty(self):
        if (self.rare == 0 and self.front==0):
            return True
        else:
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

def endeq(m,n):
    que=queue()
    for i in range(m):
        for j in range(n):
            que.enqueue(random.randint(1,1000))
        for k in range(n):
            print(que.dequeue())
            if(que.isEmpty()):
                print("Queue is reset nothing left to dequeue now.")

start = timeit.default_timer()
endeq(3,4)
stop = timeit.default_timer()
print('Time: ', stop - start)











