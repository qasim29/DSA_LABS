list=['P', 'Y', 'T', 'H', 'O', 'N']
comp=0
swap=0

for i in range(len(list)):
    val =list[i]
    found=False
    for j in range(i,len(list)):
        comp+=1
        if(val>list[j]):
            val = list[j]
            index = j
            found=True
    if(not found):
            break
    val=list[index]
    list[index]=list[i] 
    list[i]=val
    swap+=1
print(list)
print("No of Swapping: ",swap)
print("No of Comparision: ",comp)



