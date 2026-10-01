arr = list(map(int, input("enter elements with spaces ").split()))
right = len(arr) -1
left = 0
while(left < right):
    print(arr[left], arr[right])
    left += 1
    right -= 1