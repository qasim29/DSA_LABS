
list=['P', 'Y', 'T', 'H', 'O', 'N']

def insertionSort():
    comp=0
    swap=0
    for i in range(1,len(list)):
            for j in range(i,0,-1):
                comp+=1
                if(list[j]<list[j-1]):
                    val=list[j]
                    list[j]=list[j-1]
                    list[j-1]=val
                    swap+=1
                elif(list[j]>list[j-1]):
                    break
    print(list)
    print("No of Swapping: ",swap)
    print("No of Comparision: ",comp)   
insertionSort()