# Time Oct.20 2015
# A story about the chess
def totalNum(chessNum):
    sum = 0
    i =0
    while i <chessNum:
        a = 2**(i)
        sum += a*4
        i +=1
    return sum
print ('the total huge number is %d'%totalNum(64))
weight = totalNum(64)/50
weight =weight/(10**6)
print 'the wheat weight is %d Kg.'%weight
print 'the wheat weight is %d t.'%(weight/10**3)
