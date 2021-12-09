list=['P', 'Y', 'T', 'H', 'O', 'N']
comp=0
swap=0
for i in range(len(list)-1):
    j=0
    while (j<len(list)-1):
        comp+=1
        if(list[j+1]<list[j]):
            val=list[j+1]
            list[j+1]=list[j]
            list[j]=val
            j+=1
            swap+=1
        else:
            j+=1

print(list)
print("No of Swapping: ",swap)
print("No of Comparision: ",comp)



    