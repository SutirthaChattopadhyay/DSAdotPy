# Given an array of integers and a window size k, find the minimum sum of any k consecutive elements.

arr=list(map(int,input("enter array elements space separated ").split()))
k=int(input("window size "))

left = 0
right = left+k-1

cur_sum = sum(arr[left:right+1])
min_sum = cur_sum

while right < len(arr)-1:
    cur_sum = cur_sum - arr[left] + arr[right +1]

    
    left +=1
    right +=1

    if cur_sum < min_sum:
        min_sum =cur_sum

print(min_sum)        