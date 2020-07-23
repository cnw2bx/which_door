import sys
from millionaire import Millionaire

millionaire = Millionaire()
print(millionaire.compute([1,4,2,1,8])) #12
print(millionaire.compute([4,8,1])) #8
print(millionaire.compute([4,5,13,14])) #19
print(millionaire.compute([3, 7, 8, 1, 5, 10])) #21
print(millionaire.compute([0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1])) #4
print(millionaire.compute([75, 100, 75])) #150
print(millionaire.compute([1, 2, 3, 4, 5, 6])) #12
print(millionaire.compute([6, 5, 4, 3, 2, 1])) #12
print(millionaire.compute([3, 1, 2, 1000, 400, 16, 18, 69, 420, 60])) #1441
print(millionaire.compute([30, 54, 90, 63, 21, 51, 93, 28, 85, 7])) #319
print(millionaire.compute([1, 1, 1, 1, 1, 1, 1, 1])) #4
print(millionaire.compute([1])) #1
