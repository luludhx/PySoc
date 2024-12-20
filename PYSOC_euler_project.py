# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:44:43 2022

@author: dhume
"""
import numpy as np
import math as m
import pandas as pandas

''' 1- sum of multiple of 3 and 5'''
arr = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        arr.append(i)
print(np.sum(arr))


'''2- sum of even numbers in Fibonacci'''
arr = [1, 2]
even_arr = []
for y in arr:
    i = arr.index(y)
    x = arr[i] + arr[i + 1]
    if x < 4000000: 
        arr.append(x)
    else: break
for y in arr:
    if y % 2 == 0:
        even_arr.append(y)
print(np.sum(even_arr))


'''3- Largest prime factor'''
def p_nb_under(x):
    arr = []
    for num in range(1, x):
        if all(num % i != 0 for i in range(2, int(m.sqrt(num)) + 1)):
            arr.append(num)
    return arr

y = 600851475143
for i in reversed(p_nb_under(int(m.sqrt(y)) + 1)):
    if y % i == 0:
        print(i)
        break


'''4-Largest palindrome made from the product of two 3-digit numbers'''
def pal_test(x):
    decomp = [i for i in str(x)]
    rev = decomp[::-1]
    if decomp == rev:
        return True

# made a function because using return garantees breaking out of the nested loops
def b():
    for y in range(1000, 800, -1):
        for z in range(1000, 800, -1):
            x = y * z
            if pal_test(x):
                return(x)

print(b())

'''6- Sum square difference'''
sum_of_squares = sum(n**2 for n in range(101))
square_of_sums = (sum(n for n in range(101))) ** 2
print(sum_of_squares - square_of_sums)


'''7- 10 001th prime'''
arr = []
for num in range(2, 110000):
    if len(arr) <= 10001:
        if all(num % i != 0 for i in range(2, int(m.sqrt(num)) + 1)):
            arr.append(num)
    else:
        print(arr[10000])
        break


'''9- Special Pythagorean triplet'''#try to write this using numpy arrays to make it quicker
def trip():
    for x in range(1000):
        for y in range(1000):
            for z in range(1000):
                if x < y  < z:
                    if x**2 + y**2 == z**2:
                        if x + y + z == 1000:
                            return [x, y, z]
                
print(np.prod(trip()))

'''54- Poker hands'''
fname = 'poker.txt'
f = np.loadtxt(fname, dtype='str')
p1 = f[:,:5]
p2 = f[:,5:]
print(p1)
for row in p1:
    print(row)
    format(row)
    r_values = []
    r_color = []
    for c in row:
        if len(c) <= 2:
            r_values.append(c[0])
        else: r_values.append(c[0]+c[1])
        r_color.append(c[len(c)-1])
    
        
def format(r):
    for c in r:
        if c[0] == 'T':
            new = '11' + c[1]
            r.remove(c)
            r.append(new)
        if c[0] == 'Q':
            new = '12' + c[1]
            r.remove(c)
            r.append(new)
        if c[0] == 'K':
            new = '13' + c[1]
            r.remove(c)
            r.append(new)
        if c[0] == 'A':
            new = '14' + c[1]
            r.remove(c)
            r.append(new)
            
            # i cba to do this
            

'''55- Lychel numbers'''
def reverse(x):
    x = str(x)
    s = len(x)
    reverse = x[s::-1]
    reverse = int(reverse)
    return reverse
counter = 0
skip = []
iterations = 0
for x in range(10, 10000, -1):
    if any(x == i for i in skip):
        counter += 1
        continue
    y = reverse(x)
    if pal_test(x + y) is False:
        iterations += 1
        x = x + y
        y = reverse(x)
    else:
        counter += 1
        skip.extend([x,y])
    if iterations == 50:
            break
print(counter)


    
    



        