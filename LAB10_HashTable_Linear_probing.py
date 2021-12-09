import random

class student():
    def __init__(self,regNO,name,courses,cgpa):
        self.regNO=regNO
        self.name=name
        self.courses=courses
        self.cgpa=cgpa
    def toString(self):
        return f"  {self.regNO}\t    {self.name}\t {self.courses}\t   {self.cgpa}"


class hashTable():
    def __init__(self):
        self.list=[]
        self.count=0
        self.initializelist()
       
    def initializelist(self):
        for i in range(50):
            self.list.append(0)
    
    def hash(self,obj):
        keyHash= (obj.regNO)%50
        k=1
        while (self.list[keyHash]!=0):
                keyHash = (keyHash+k)%50
                k+=1
        return keyHash
    
    def add(self,obj):
            index=self.hash(obj)
            self.list[index]=obj
            self.count+=1

    def traverse(self):
        c=0
        print("{INDEX} | {regNO} | {name} | {courses} | {cgpa}")
        for i in self.list:
            if(i!=0):
                print("  "+str(c) +"\t  "+ i.toString())
            else:
                print("  "+str(c)+"\t    None    None\tNone\t  None")
            c+=1

    def search_Hash(self,regNO):
        index =regNO%50 
        subcount=0
        while(subcount != self.count and self.list[index]!=0):
            if(self.list[index].regNO==regNO):
                return index
            index+=1
            subcount+=1
        return -1

    def search(self,regNO):
        index =regNO%50 
        if(self.search_Hash(regNO)==-1):
            print(f"Student with regNO {regNO} Not Found\n")
        else:
            print(f"Student with regNO {regNO} Found\n")
                    
    def remove(self,regNO):
        index =regNO%50 
        val=self.search_Hash(regNO)
        if(val==-1):
                print(f"Student with regNO {regNO} Not Found\n")
        else:
            del self.list[val]
            self.list.insert(val,0)
            print(f"Student with regNO {regNO} deleted\n")

    def update(self,obj):
        val=self.search_Hash(obj.regNO)
        if(val==-1):
                print(f"Student with regNO {obj.regNO} Not Found\n")
        else:
            self.list[val]=obj
            print(f"Student with regNO {obj.regNO} updated\n")
        
    def size(self):
        return self.count

    def isEmpty(self):
        if(self.count==0):
            return True
        else:
             False

obj=hashTable()
for i in range(40,20,-1):
    x=str(i)+"qasim"
    obj.add(student((i*3)-1,x,10,random.randint(0,5)))
obj.traverse()
obj.search(798)
obj.update(student(98,"abdullah",10,4))
obj.remove(95)
obj.add(student(55,"abdullah",10,4))
obj.add(student(105,"abdullah",10,4))
obj.traverse()
print(f"The Length is: "+ str(obj.size()))
print(f"Hash Table is Empty: "+ str(obj.isEmpty()))


