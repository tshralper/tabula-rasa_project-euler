# -*- coding: utf-8 -*-
"""
!!!!!!Not finished!!!!!!

Created on Wed Aug 15 15:22:37 2018

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
@author: tlane
"""

#Ask for number
raw = input('Enter number ')
if raw == '': raw = 13195
num = int(raw)

#Determine factors
factors = list()
divisor = 0

while divisor < (num+1):
    divisor = divisor + 1
    if num % divisor == 0:
        factors.append(divisor)
        pair = int(num / divisor)
        if pair in factors: break
        factors.append(pair)
sortFactors = sorted(list(factors))         
print(sortFactors)

#Determine what factors are prime
rFactors = list(reversed(sortFactors))
print(rFactors)
for factor in rFactors:
    divisor = 1
    while divisor < (factor + 1):
        fFactor = list()
        divisor = divisor + 1
        if factor % divisor == 0:
            fFactor.append(divisor)
        print(fFactor)