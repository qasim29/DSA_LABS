class stack():
    def __init__(self):
        self.list=[]
        self.count=0
    def push(self,val):
        self.list.append(val)
        self.count+=1
    def pop(self):
        self.count-=1
        return self.list.pop()

def isNumeric(val):
    val=val.strip()
    try:
        num=float(val)
        return True
    except:
        return False
c=1
sta=stack()
while(True):
    print("enter input: ")
    print("for answer enter print")
    a=str(input()) 
    if(c%2!=0 and isNumeric(a)):
        sta.push(float(a))     
    elif(c%2==0 and (a=='*' or a=="+") ):
        sta.push(a)
    elif(a.lower()=="print"):
        c=sta.pop()
        d=sta.pop()
        e=sta.pop()
        if(d=="*"):
            print(c*e)
        if(d=="+"):
            print(c+e)
        break
    else:
        print("bad input")
    c+=1

    


    