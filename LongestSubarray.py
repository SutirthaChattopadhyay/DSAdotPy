# Given an array of positive integers and a target k, find the length of the longest contiguous subarray whose sum is less than or equal to k.
arr = list(map(int,input("enter array ").split()))
k = int(input("target "))

left = 0
curr_sum = 0
max_lenght = 0

for right in range(len(arr)):
    curr_sum += arr[right]

    while curr_sum > k :
        curr_sum -= arr[left]
        left += 1

    length = right - left +1

    if length >max_lenght:
        max_lenght = length 


print(max_lenght)