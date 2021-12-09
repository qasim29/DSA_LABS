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

str ='qasim'
sta=stack()
temp=""
for i in range(len(str)):
    sta.push(str[i])
for i in range(len(str)):
    temp+=sta.pop()  
print(temp)
