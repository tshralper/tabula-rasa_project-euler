# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:22:37 2018

The prime factors of 13195 are 5, 7, 13 and 29.

Problem: What is the largest prime factor of the number 600851475143 ?

Answer: 6857
    
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

#Determine what factors are prime
rFactors = list(reversed(sortFactors))
fFactors = list()

for factor in rFactors:
    divisor = 1
    while divisor < (factor + 1):
        divisor = divisor + 1
        if factor % divisor == 0 and divisor < factor: break
        elif divisor == factor:
            fFactors.append(divisor)
print(max(fFactors))