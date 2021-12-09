class node():
    def __init__(self,val1):
        self.next=None
        self.val=val1

class linkedlist():
    def __init__(self) -> None:
        self.count=0
        self.head=None
        self.tail=None
    def add(self,val):
        obj=node(val)
        if(not self.isEmpty()):
            self.tail.next=obj
            self.tail=self.tail.next
            self.count+=1
        else:
            self.head=obj
            self.tail=self.head
            self.count+=1
    def deletefirst(self):
        if(not self.isEmpty()):
            self.head=self.head.next
        else:
            print("already empty")
    def traverse(self):
        temp=self.head
        for i in range(self.count):
            print(temp.val)
            temp=temp.next
    def isEmpty(self):
        if(self.count==0):
            return True
        else:
            False   

list=linkedlist()
for i in range(10):
    list.add(i)
list.traverse()