## Adding elements to a list
numbers = [1, 2, 3]

numbers.append(4)
# [1, 2, 3, 4]

numbers.extend([5, 6])
# [1, 2, 3, 4, 5, 6]

numbers.insert(1, 99)
# [1, 99, 2, 3, 4, 5, 6]

# Method :
# 1. append(x)                adds x as on element
# 2. extend(iterable)         adds each element from an iterable
# 3. insert(i, x)             inserts x at index i 

a = [1,2]
a.append([3,4])
# [1, 2, [3,4]]

b = [1,2]
b.extend([3,4])
# [1, 2, 3, 4]

# MUTABLE VS IMMUTABLE

# mutable:- an object whose contents can be changed after creation
#  1.list
#  2.dict
#  3.set

# immutable:- an object whose contents cannot be changed after creation
#  1.int
#  2.float
#  3.str
#  4.bool
#  5.tuple

numbers = [1, 2, 3]
numbers[0] = 10  #valid

values = (1,2,3)
values[0] = 10   #type error

# The tricky tuple case 
x= (1,2,[3,4])
x[2].append(5)

print(x)
#(1,2,[3,4,5])

# Why does this work?

# the tuple is immutable, but the list stored inside it is mutable. 
# You cannot replace the tuple's element, but you can modify the liat object refers to.

arr = 