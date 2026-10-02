# 1. Find first zero → left
# 2. right scans ahead
# 3. right finds non-zero → swap
# 4. move both
# 5. right finds zero → keep scanning


arr = list(map(int, input("enter elements with spaces ").split()))

# left =0 
# right = left+1
n = len(arr)

for i in range(len(arr)):
    if(arr[i] == 0):
        left = i
        right = left+1
        break


while (right < n):
    if(arr[right] == 0):
        right +=1
    else:
        temp = arr[right]
        arr[right] = arr[left]
        arr[left] = temp
        right +=1
        left +=1    
    
print(arr)