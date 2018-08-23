'''
Created on Thurs Aug 23 12:16:00 2018

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Problem: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 25164150

@author: tlane
'''

#Ask for number natural numbers to test
raw = input('First how many natty numbs? ')
if raw == '': raw = 10
nattyNum = int(raw)

#Find the sum of squares
listOfSquares = [n**2 for n in range(1, (nattyNum + 1))]
sumOfSquares = sum(listOfSquares)

#Find the square of sums
listOfSums = [n for n in range(1, (nattyNum + 1))]
squareOfSums = sum(listOfSums)**2

#Find the diference between the sum of squares and square of sums
difference = squareOfSums - sumOfSquares
print(difference)
