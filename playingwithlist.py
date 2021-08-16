import math
import numpy as np
def countlength(listone):
    x = len(listone)
    print("the list is consisted of ")
    for j in listone:
        print(j)
    print("The size of the list is")
    return x
def maxandminval(listone):
    y = max(listone)
    z = min(listone)
    print("The max and min value respectively are ")
    return y,z
def avgandsum(listone):
    avg = np.mean(listone)
    total = np.sum(listone)
    print("The average and sum of the list are ")
    return avg,total
def mostfrequent(listone):
    frequent = np.bincount(listone)
    val = np.argmax(frequent)
    print("The most frequent value in the list is")
    return val
def sortingthelist(listone):
    ascending = np.array(listone)
    ascending = sorted(listone, reverse=False)
    descending = np.array(listone)
    descending = sorted(listone, reverse=True)
    print("The sorted list in ascending and descending order respectively are ")
    return ascending, descending
def addthelist(listone,newelement):
    new = listone + newelement
    print("The new list is ")
    return new
def doublethelist(listone):
    d = [c * 2 for c in listone]
    print("The double of the list is ")
    return d
def tripplethelist(listone):
    t = [a * 3 for a in listone]
    print("The tripple of the list is ")
    return t
def squarethelist(listone):
    s = [i ** 2 for i in listone]
    print("The square of the list is ")
    return s
def cubethelist(listone):
    cube = [j ** 3 for j in listone]
    print("The cube of the list is ")
    return cube
def halfthelist(listone):
    half = [b/2 for b in listone]
    print("The half of the list is ")
    return half
# Testing the function
print(countlength([1,8,9]))
print(maxandminval([1,8,9]))
print(avgandsum([1,8,9]))
print(mostfrequent([1,2,2]))
print(sortingthelist([3,7,6]))
print(addthelist([1,2,3],[4,5]))
print(doublethelist([2,3]))
print(tripplethelist([1,4,6]))
print(squarethelist([2,4,6]))
print(cubethelist([2,4,6]))
print(halfthelist([2,8,10]))