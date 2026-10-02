arr = list(map(int,input().split()))

large = arr[0]
sec_large = large

small = arr[0]
sec_small = small

for i in range(1,len(arr)):
    if arr[i]>large:
        sec_large = large
        large = arr[i]

        
        

print(large)    
print(sec_large)     