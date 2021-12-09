class queue():
    def __init__(self) -> None:
        self.count=0
        self.list=[]
    def enqueue(self,val):
        self.list.insert(0,val)
        self.count+=1
    def dequeue(self):
        self.count-=1
        return self.list.pop()
    def size(self):
        return self.count
    def traverse(self):
        for i in range(len(self.list)-1,-1,-1):
            print(self.list[i])

def merge(que1,que2):
    que=queue()
    for i in range(que1.size()):
        que.enqueue(que2.dequeue())
        que.enqueue(que1.dequeue())
    return que

def main():
    que1=queue()
    que2=queue()
    for i in range(2,9,2):
        que1.enqueue(i) 
    for i in range(1,8,2):
        que2.enqueue(i)
    merge(que1,que2).traverse()

main()
     

        



