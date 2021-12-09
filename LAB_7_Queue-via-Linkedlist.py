# import timeit

class node():
    def __init__(self,val,obj):
        self.next = obj 
        self.val =  val

class linkedlist():        

    def __init__(self) :            
        self.head = None
        self.tail= None
        self.count = 0
    
    def isEmpty(self):
        if self.count==0: return True
        else: return False

    def size(self):
        return self.count

    
    def clear(self):
        if(not self.isEmpty()):
            for i in range(self.count):
                self.deletefirst()
        else:
            print("linkedList already empty")

    def insertFirst(self,val):
        if (not self.isEmpty()):
            self.head = node(val,self.head)
            self.count+=1      
        else:
            self.head = node(val,None)   
            self.tail = self.head
            self.count+=1

    def insertLast(self,val):    
        if (not self.isEmpty()):
            self.tail.next = node(val,None)
            self.tail = self.tail.next
            self.count+=1      
        else:
            self.head = node(val,None)   
            self.tail = self.head
            self.count+=1   
    
    def deletefirst(self):
            if(not self.isEmpty()):
                pointer=self.head.next
                del self.head
                self.head = pointer
                self.count-=1
            else:
                print("No element present in linkedList") 

    def deleteLast(self):
        if(not self.isEmpty()):
            pointer=self.head
            for i in range(self.count-1):
                pointer = pointer.next
            del pointer.next
            self.tail=pointer 
            self.count-=1     
        else:
            print("No element present in linkedList")

    def traverse(self):
        if(not self.isEmpty()):
            pointer=self.head
            for i in range(self.count):
                print(pointer.val)
                pointer = pointer.next
        else:
            print("No element present in linkedList")

class queue() :
    
    def __init__(self) :
        self.link=linkedlist()
        
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

