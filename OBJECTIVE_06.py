class stack():
    def __init__(self) -> None:
        self.count=0
        self.list=[]
    def push(self,val):
        self.list.append(val)
        self.count+=1
    def pop(self):
        self.count-=1
        return self.list.pop()
    def isEmpty(self):
        if(self.count==0):
            return True
        else :
            return False
    def traverse(self):
        if(not self.isEmpty()):
            for i in range(len(self.list)-1,-1,-1):
                print(self.list[i])

def evaluate(op2,op1,ope):
    print(op1+ope+op2)
    return str(eval(op1+ope+op2))

def main():
    sta =stack()
    exp="12+34*-9/"

    for i in exp:
        if(ord(i)>=48 and ord(i)<=57):
            sta.push(i)
        elif(i=='+' or i=='-' or i=='*' or i=='/'):
            sta.push(evaluate(sta.pop(),sta.pop(),i))
            sta.traverse()    

main()

