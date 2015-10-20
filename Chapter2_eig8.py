# Time Oct.20 2015
# A simple input to judge whether prime number
from math import *
a = raw_input('Input an integer:')
while True:
    if not a.isdigit():
        print 'Error: try again.'
        a = raw_input('Input an integer:')
    else:
        print 'The integer is:%s'%a
        break
b = int(a)
N = int(sqrt(b))
i = 2
while i <= N:
    if b%i ==0:
        print 'The input can be divided by %d'%i
    i+=1


