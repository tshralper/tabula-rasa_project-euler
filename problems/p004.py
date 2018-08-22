'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Problem: Find the largest palindrome made from the product of two 3-digit
numbers.

Answer: 906609

@author: tlane
'''
#Multiply two, three digit numbers together systematically. Make a list of palindromes. Print the max
num1 = 100
palins = list()

while num1 < 1000:
    num2 = 100
    while num2 < 1000:
        mult = str(num1 * num2)
        if mult[0] == mult[len(mult)-1]:
            if mult[1] == mult[len(mult)-2]:
                if mult[2] == mult[len(mult)-3]:
                    palins.append(int(mult))
        num2 = num2 + 1
    num1 = num1 + 1

print(max(palins))
