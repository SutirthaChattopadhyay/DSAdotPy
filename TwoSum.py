# Given an array of integers nums 
# and a target target, return the 
# indices of two numbers whose sum equals the target.

# nums = [2, 7, 11, 15]
# target = 9

nums = list(map(int,input("enter elements ").split()))
target = int(input("enter target variable "))
seen = {}

for i in range(len(nums)):
    compement = target - nums[i]

    if compement in seen:
        print([seen[compement], i])
        break

    


    seen[nums[i]] = i 

