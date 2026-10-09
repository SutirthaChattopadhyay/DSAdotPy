# Write Python code to find the maximum sum of any k consecutive elements

arr = list(map(int, input("enter elements with spaces ").split()))
k = 3 #can be user defined

left=0
right=left+k-1

curr_sum = sum(arr[left:right +1])
max_sum=curr_sum

while right < len(arr) - 1:
    curr_sum = curr_sum -arr[left] + arr[right + 1]

    left +=1
    right +=1

    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
