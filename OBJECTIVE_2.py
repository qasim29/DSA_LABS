class stack():
    def __init__(self) -> None:
        self.list=[]
        self.count=0
    def push(self,val):
        self.list.append(val)
        self.count+=1
    def pop(self):
        self.count-=1
        return self.list.pop()
    def isEmpty(self):
        if(self.count==0):
            return True
        else:
            False
    def top(self):
        return self.list[-1]
    def traverse(self):
        for i in self.list:
            print(i)
    
class queue():
    def __init__(self) -> None:
        self.count=0
        self.list=[]
    def enqueue(self,val):
        self.list.insert(0,val)
        self.count+=1
    def dequeue(self,val):
        self.list.pop()
        self.count-=1
    def peek(self):
        return self.list[-1]
    def isEmpty(self):
        if(self.count==0):
            return True
        else:
            False
    def traverse(self):
        for i in range(len(self.list)-1,-1,-1):
            print(self.list[i])

sta=stack()
que=queue()
for i in range(1,11):
    sta.push(i)
sta.traverse()
for i in range(1,11):
    que.enqueue(sta.pop())
que.traverse()