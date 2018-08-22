'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

Answer: 232792560
Program completes in less than 10 seconds. Could it be sped up?

@author: tlane
'''

#Ask for input of number range
raw = input('Range from 1 to _')
if raw == '': raw = 10
end = int(raw)

#Make a list of numbers in the range
rng = list(range(1,(end + 1)))
largest = rng[len(rng) - 1]

#Check numbers incrementally and find out which one is divisible by all numbers in the range
num = 0 + largest
lcd = None
gnr = list(reversed(rng))

while lcd == None:
    goal = 0
    for n in gnr:
        if num % n != 0: break
        goal = goal + 1
        if goal == len(gnr):
            lcd = num
    num = num + largest

print(lcd)
