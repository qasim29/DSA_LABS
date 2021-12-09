class Node():

    def __init__(self,val,obj1,obj2):
        self.val=val
        self.objback=obj1
        self.objnext=obj2

class Linkedlist():
    
    def __init__(self):
        self.count=0
        self.head:None
        self.tail:Node

    def isEmpty(self):
        if(self.count==0):
            return True
        else: 
            return False

    def initialize(self,val):
            self.head=Node(val,None,None)
            self.tail=self.head
            self.count+=1

    def insertFirst(self,val):
        if(self.isEmpty()):
            self.initialize(val)
        else:
            self.head.objback=Node(val,None,self.head)
            self.head=self.head.objback
            self.count+=1

    def insertLast(self,val):
        if(self.isEmpty()):
            self.initialize(val)
        else:
            self.tail.objnext=Node(val,self.tail,None)
            self.tail=self.tail.objnext
            self.count+=1

    def traverse(self):
        if(self.isEmpty()):
            print("linkedlist is empty")
        else:
            point = self.tail
            for i in range(self.count):
                print(point.val)
                point= point.objback

    def deleteLast(self):
        if(self.isEmpty()):
            print("already empty")
        else:
            self.tail=self.tail.objback
            del self.tail.objnext
            self.count-=1
    
    def deleteFirst(self):
        if(self.isEmpty()):
            print("already empty")
        else:
            self.head=self.head.objnext
            del self.head.objback
            self.head.objback=None
            self.count-=1

class queue() :
    
    def __init__(self) :
        self.link=Linkedlist()
        
    def enqueue(self,val):
       self.link.insertFirst(val)
    
    def dequeue(self):  
        if (not self.isEmpty()):
            return self.link.deleteLast()
        else: 
            print("queue already empty")     
    
    def traverse(self):
        self.link.traverse() 

    def isEmpty(self):
        if (self.link.isEmpty()):
            return True
        else: 
            return False
    def len(self):
        if (not self.isEmpty()):
            return self.link.size()
        else:
            print("queue is empty")     
            return 0 
 
    def peek(self):
        if(not self.isEmpty()):
             return self.link.tail.val
        else:
            print("Queue is empty")      

def main():

    a = queue()
    print("\nTo enqueue in queue press: 1\nTo dequeue from queue press: 2"
        "\nTO Check if empty press: 3\nTo get the top press: 4"
        "\nTo get the length press: 5"
        "\nTo Exit press: 6")
    while(True):
        b = int(input("Enter your choice: "))
        if(b==1):
            c=int(input("Enter the number: "))
            a.enqueue(c)
            print("printing queue")
            a.traverse()
        elif (b==2):
            a.dequeue()
            if(not a.isEmpty()):
                print("printing queue")
                a.traverse()
                print("end queue")
        elif(b==3):
            print("queue is empty: ",a.isEmpty())
        elif(b==4):
            print("The Top is: ",a.peek())
        elif(b==5):
            print("The length is: ",a.len())
        elif(b==6):
            print("bye !!!")
            break
        else: print("please choose the correct option")    

main()


link =Linkedlist()
link.insertLast(1)
link.insertLast(2)
link.insertFirst(3)
link.deleteFirst()
link.deleteLast()
link.traverse()
