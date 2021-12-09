class stack():
    def __init__(self) -> None:
        self.list=[]
        self.count=0
    def push(self,val):
        self.list.append(val)
        self.count+=1
    def pop(self):
        if(not self.isEmpty()):
            self.count-=1
            return self.list.pop()
        else:
            print("nothing")
    def isEmpty(self):
        if(self.count==0):
            return True
        else:
            return False
    def size(self):
        return self.count
    def top(self):
        if(self.isEmpty()):
            return False
        else:
             return self.list[-1]

def checkPrecedence(op,top):
    dict = {
        "(":6,
        "^":5,
        "*":4,
        "/":4,
        "+":3,
        "-":3,
    }
    if(top==False):
        return True
    if(top=="(" or dict[top]<dict[op] or op=='^'):
        return True
    else:
        return False

def getPostFix(exp):
    temp=""
    sta=stack()
    for i in range(len(exp)):
        if((ord(exp[i])>=65 and ord(exp[i])<=90) or
            (ord(exp[i])>=97 and ord(exp[i])<=122) or
            (ord(exp[i])>=48 and ord(exp[i])<=57)):
            temp=temp+exp[i]
        elif(exp[i]==")"):
            while(True):
                if(sta.top()=="("):
                    sta.pop()
                    break
                temp=temp+sta.pop()    
        elif(checkPrecedence(exp[i],sta.top())):    
            sta.push(exp[i])
        else:
            while(not checkPrecedence(exp[i],sta.top())):
                temp=temp+sta.pop()
            sta.push(exp[i])
    while(not sta.isEmpty()):
        temp=temp+sta.pop()
    return temp

def main():
    exp="a-b+(m^n)*(o+p)-Q/r^S*T+z^y^u"
    print(getPostFix(exp))

main()


