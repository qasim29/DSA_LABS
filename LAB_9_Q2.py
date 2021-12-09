import math
import random
class student():
    def __init__(self,regNO,name,courses,cgpa):
        self.regNO=regNO
        self.name=name
        self.courses=courses
        self.cgpa=cgpa
def search_Via_LinearSearch(list,val):
    for i in list:
        ok=False
        if(i.regNO==val):
            print("Studet Regesteration No: ", i.regNO)
            print("student name: ", i.name)
            print("student no. of courses: ", i.courses)
            print("student cgpa: ",i.cgpa)
            ok=True
            break
    if(not ok):
        print(f"Regesteration No.{val} not found ")
def dataSort_Via_BubbleSort(list):
        for i in range(len(list)):
            swap=False
            for j in range(len(list)-1-i):
                if(list[j].regNO>list[j+1].regNO):
                    swap=list[j+1]
                    list[j+1]=list[j]
                    list[j]=swap
                    swap=True
            if(not swap):
                break
def search_Via_BinarySearch(list,x):
    ub=len(list)-1
    lb=0
    while(ub>=lb):
        mid = math.floor((ub+lb)/2)
        a=list[mid].regNO
        if(list[mid].regNO==x):
            print("Studet Regesteration No: ", list[mid].regNO)
            print("student name: ", list[mid].name)
            print("student no. of courses: ", list[mid].courses)
            print("student cgpa: ",list[mid].cgpa)
            break
        if(x>list[mid].regNO):
            lb=mid+1
        else:
            ub=mid-1
def dataSort_Via_InsertionSort(list):
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if(list[j].cgpa>list[j-1].cgpa):
                swap=list[j-1]
                list[j-1]=list[j]
                list[j]=swap
list=[]
for i in range(5,-1,-1):
    x=str(i)+"qasim"
    list.append(student(i,x,10,random.randint(0,5)))
print("Unmodified Data")
for i in list:
    print(f"regNo={i.regNO} cgpa={i.cgpa}",)

print("using bubble sort to sort for regNO")
dataSort_Via_BubbleSort(list)
for i in list:
    print(f"regNo={i.regNO} cgpa={i.cgpa}",)

print("using Binary search to search for regNO=4")
search_Via_BinarySearch(list,4)

print("using liear search to search for regNO=5")
search_Via_BinarySearch(list,5)

print("using selection sort to sort for cgpa")
dataSort_Via_InsertionSort(list)
for i in list:
    print(f"regNo={i.regNO} cgpa={i.cgpa}",)