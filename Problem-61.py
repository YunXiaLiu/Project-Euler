# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:50:16 2016

@author: Xiaotao Wang
"""

"""
Problem 61:

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
all figurate (polygonal) numbers and are generated by the following formulae:

Triangle     P(3,n)=n(n+1)/2     1, 3, 6, 10, 15, ...
Square       P(4,n)=n2           1, 4, 9, 16, 25, ...
Pentagonal   P(5,n)=n(3n−1)/2    1, 5, 12, 22, 35, ...
Hexagonal    P(6,n)=n(2n−1)      1, 6, 15, 28, 45, ...
Heptagonal   P(7,n)=n(5n−3)/2    1, 7, 18, 34, 55, ...
Octagonal    P(8,n)=n(3n−2)      1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

1.The set is cyclic, in that the last two digits of each number is the first
  two digits of the next number (including the last number with the first).
2.Each polygonal type: triangle (P(3,127)=8128), square (P(4,91)=8281), and
  pentagonal (P(5,44)=2882), is represented by a different number in the set.
3.This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal, is represented by a different number in the set.
"""

def genTriangle(minnum, maxnum):
    
    i = 1
    n = 1
    while n <= maxnum:
        if n >= minnum:
            yield n
        i += 1
        n = i * (i + 1) // 2

def genSquare(minnum, maxnum):
    
    i = 1
    n = 1
    while n <= maxnum:
        if n >= minnum:
            yield n
        i += 1
        n = i ** 2

def genPentagonal(minnum, maxnum):
    
    i = 1
    n = 1
    while n <= maxnum:
        if n >= minnum:
            yield n
        i += 1
        n = i * (3*i - 1) // 2

def genHexagonal(minnum, maxnum):
    
    i = 1
    n = 1
    while n <= maxnum:
        if n >= minnum:
            yield n
        i += 1
        n = i * (2*i - 1)

def genHeptagonal(minnum, maxnum):
    
    i = 1
    n = 1
    while n <= maxnum:
        if n >= minnum:
            yield n
        i += 1
        n = i * (5*i - 3) // 2

def genOctagonal(minnum, maxnum):
    
    i = 1
    n = 1
    while n <= maxnum:
        if n >= minnum:
            yield n
        i += 1
        n = i * (3*i - 2)    
    

def search():
    
    RawDict = {3: list(genTriangle(1000, 9999)), 4: list(genSquare(1000, 9999)),
               5: list(genPentagonal(1000, 9999)), 6: list(genHexagonal(1000, 9999)),
               7: list(genHeptagonal(1000, 9999)), 7: list(genOctagonal(1000, 9999))}
    
    digitBase = {}
    for k in RawDict:
        for v in RawDict[k]:
            if v in digitBase:
                digitBase[v].add(k)
            else:
                digitBase[v] = set([k])
    
    for v in digitBase:
        chain = [v]
        pool = {i+1: digitBase.keys() for i in range(len(RawDict)-1)}
        Sets = [set([i]) for i in digitBase[v]]
        # Make it possible for communications between loops
        cache_pool = {}
        cache_sets = {}
        candicates = pool[len(chain)][:]
        while len(chain) < len(RawDict):
            while len(candicates):
                c = candicates.pop()
                if c in chain:
                    continue
                else:
                    check_last = chain[-1] % 100
                    check_cur = c // 100
                    if check_last != check_cur:
                        continue
                    curclass = digitBase[c]
                    tmpsets = []
                    for rs in Sets:
                        for cs in curclass:
                            union = set([cs]) | rs
                            if len(union) >= len(chain):
                                tmpsets.append(union)
                    if len(tmpsets):
                        # Snapshot of the current loop
                        cache_pool[len(chain)] = candicates
                        cache_sets[len(chain)] = Sets
                        chain.append(c)
                        Sets = tmpsets
                        # Initialization for next loop
                        candicates = pool[len(chain)][:]
                        break
            
            if len(candicates) == 0:
                if len(chain) == 1:
                    break
                else:
                    chain.pop()
                    # Return to the stop point of the last loop
                    candicates = cache_pool[len(chain)]
                    Sets = cache_sets[len(chain)]
        
        if len(chain) == 6:
            check_last = chain[-1] % 100
            check_first = chain[0] // 100
            if check_first == check_last:
                return chain

if __name__ == '__main__':
    chain = search()