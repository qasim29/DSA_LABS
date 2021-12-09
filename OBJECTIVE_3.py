class stack():
    def __init__(self):
        self.count=0
        self.list=[]
    def push(self,val):
        self.list.append(val)
        self.count+=1
    def pop(self):
        self.list.pop()
        self.count-=1
    def isEmpty(self):
        if(self.count==0):
            return True
        else:
            return False
    def traverse(self):
        for i in range(len(self.list)-1,-1,-1):
            print(self.list[i])

class queue():
    def __init__(self) -> None:
        self.count=0
        self.list=[]
    def enqueue(self,val):
        self.list.append(val)
        self.count+=1
    def dequeue(self):
        self.count-=1
        return self.list.pop(0)
    def peek(self):
        return self.list[0]
    def traverse(self):
        for i in self.list:
            print(i)

sta=stack()
que=queue()

for i in range(10):
    que.enqueue(i)

for i in range(10):
    temp = que.dequeue()
    sta.push(temp)
    que.enqueue(temp)
    
sta.traverse()
que.traverse()
