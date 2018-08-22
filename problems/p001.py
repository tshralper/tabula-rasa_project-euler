
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168

@author: tlane
'''
import numpy as np

#Generate a multiplication array
mult = np.array(range(1,350))

#Generate arrays of multiples of 3's and 5's
threes = 3 * mult
fives = 5 * mult

#Make list of multiples that are below 1000
nums = list()

for num in threes:
    if num < 1000:
        nums.append(num)

for num in fives:
    if num < 1000:
        nums.append(num)

#Sum all multiples less than 1000
nums = list(set(nums)) #removes duplicates
total = sum(nums)
print(total)
