class stack():
    def __init__(self) -> None:
        self.count=0
        self.list=[]
    def push(self,val):
        self.list.append(val)
        self.count+=1
    def pop(self):
        self.count-=1
        self.list.pop()
    def isEmpty(self):
        if(self.count==0):
            return True
        else:
            return False    
str="(()())((((()))))"
sta=stack()
for i in range(len(str)):
    if(str[i]=='('):
        sta.push(str[i])
    elif(str[i]==')'):
        sta.pop()
if(sta.isEmpty()):
    print("it is balanced")
else:
    print("it is not balanced ")    
        