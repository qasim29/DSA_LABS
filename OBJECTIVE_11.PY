class contact():
    def __init__(self,num,name) -> None:
        self.number=num
        self.name=name
    def toString(self):
        return f"Name: {self.name} , Number: {self.number}"

class node():
    def __init__(self,obj) -> None:
        self.next=None
        self.back=None
        self.val=obj

class linkedlist():
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.count=0
    def add(self,contact):
        obj=node(contact)
        if(not self.isEmpty()):
            self.tail.next=obj
            obj.back=self.tail
            self.tail=self.tail.next
            self.count+=1
        else:
            self.head=obj
            self.tail=self.head
            self.count+=1
    def isEmpty(self):
        if(self.count==0):
            return True
        else:
            return False
    def deletelast(self):
        if(not self.isEmpty()):
            self.tail=self.tail.back
            del self.tail.next
        else:
            print("list is already empty")
    def traverse(self):
        temp=self.head
        for i in range(self.count):
            print(temp.val.toString())
            temp=temp.next
    
list=linkedlist()
for i in range(10):
    list.add(contact("0300216251"+str(i),"qasim"+str(i)))    
list.traverse()
