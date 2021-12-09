
#separate chaining
import random


class student():
    def __init__(self,regNO,name,courses,cgpa):
        self.regNO=regNO
        self.name=name
        self.courses=courses
        self.cgpa=cgpa
    def toString(self):
        print(f"  {self.regNO}\t  {self.name}     {self.courses}\t {self.cgpa}")

class hashTable():
    
    def __init__(self):
        self.list=[]
        self.count=0
        self.initializelist()
       
    def initializelist(self):
        for i in range(20):
            self.list.append([0])
        
    def hash(self,obj):
        index= (obj.regNO)%20
        return index
    
    def search_Hash(self,val):
        index= val%20
        return index

    def add(self,obj):
        index=self.hash(obj)
        self.list[index].clear()
        self.list[index].append(obj)
    
    def search(self,val):
        index = self.search_Hash(val)
        for i in self.list[index]:
            if(i.regNO==val):
                print(f"Student with regNO {val} Found\n")
                break
            else:
                print(f"Student with regNO {val} Not found\n")
    
    def traverse(self):
        print("{regNO} | {name} | {courses} | {cgpa}")
        for i in self.list:
            for j in i:
                j.toString()

    def remove(self,val):
        index = self.search_Hash(val)
        for i in range(len(self.list[index])):
            if(self.list[index][i].regNO==val):
                del self.list[index][i]
                print(f"student with regNo {val} deleted")
                break
            else:
                print("not found")
    
    def update(self,obj):
        index=self.hash(obj)
        for i in range(len(self.list[index])):
            if(self.list[index][i].regNO==obj.regNO):
                 self.list[index][i]=obj
        
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
obj.search(119)
obj.search(115)
obj.update(student(98,"abdullah",10,4))
obj.traverse()



