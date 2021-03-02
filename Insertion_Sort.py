# Insertion Sort Algorithm

list=[]
n=int(input("Enter total elements in a list:"))
for i in range(n):
    a=int(input("Enter element :"))
    list.append(a)
print("\n")    
print("Unsorted list:",list)    
print("\n")
def insertionsort(list): 
    for i in range(1,len(list)): 
        a = list[i] 
        j = i-1
        while j>=0 and a<list[j] : 
                list[j+1] = list[j] 
                j = j-1
        list[j+1] = a
        print("PASS ",i,list)
    return ""
        
print(insertionsort(list))
print("Sorted List:",list)
