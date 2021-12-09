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
    
str="abcdcba"
sta=stack()
for i in str:
    sta.push(i)
temp=""
for i in str:
    temp+=sta.pop()
if(str==temp):
    print("its a palindrome string")
else:
    print("not a palindrome string")
