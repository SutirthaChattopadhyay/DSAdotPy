# This code helps to find the frequncy of the numbers in a given array of integers


arr = list(map(int, input().split()))
freq = {}
max_freq = 0
most_freq  = 0

for x in arr:
    freq[x] = freq.get(x,0)+1
print(freq)

for numbers, frequency in freq.items():
    if frequency > max_freq:
        max_freq = frequency
        most_freq = numbers
print(most_freq)        
print(max_freq)