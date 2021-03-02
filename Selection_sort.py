list=[]
n=int(input("Enter total elements in a list:"))
for i in range(n):
    a=int(input("Enter element :"))
    list.append(a)
print("\n")    
print("Unsorted List:",list)    
print("\n")

def selectionsort(list):
    for i in range(len(list)-1): 
        minimum = i
        for j in range(i+1,len(list)):
            if list[j] < list[minimum] :
                minimum = j
        list[i],list[minimum] = list[minimum],list[i]
        print("PASS ",i+1,list)
    return ""
        
print(selectionsort(list))
print("Sorted List:",list)
    
    


