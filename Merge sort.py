list=[]
n=int(input("Enter total elements in a list:"))
for i in range(n):
    a=int(input("Enter element :"))
    list.append(a)
print("\n")    
print("Unsorted List:",list)    
print("\n")

def merge_sort(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    print("Splitting: ",left,right)

    left = merge_sort(left)
    right = merge_sort(right)
    print(left,right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:]) 
        print("Merging   : ",result)
    return result

print("\n","Sorted List: ", merge_sort(list))
