# time Oct.20 2015
# a regular arithmetic examples
print '= '*10 +'start eigth'+'= '*10
def eigth(num):
    a =range(1,10)
    b=[ str(i) for i in a]
    c =''.join(b)
    for i in range(9):
        a1 = int(c[:i+1:])
        b1 = num
        c1 = a1*b1 +i+1
        print "%d*%d+%d=%d"%(a1,b1,i+1,c1)
eigth(8)
print '= '*10 +'end eigth'+'= '*10
print '= '*20
print '= '*10 +'start nine'+'= '*10
def nine(num):
    a =range(1,10)
    b=[ str(i) for i in a]
    c =''.join(b)
    for i in range(9):
        a1 = int(c[:i+1:])
        b1 = num
        c1 = a1*b1 +i+2
        print "%d*%d+%d=%d"%(a1,b1,i+2,c1)
nine(9)
print '= '*10 +'end nine'+'= '*10
print '= '*20
print '= '*10 +'start nine'+'= '*10
def nine1(num):
    a =range(9,1,-1)
    b=[ str(i) for i in a]
    c =''.join(b)
    for i in range(8):
        a1 = int(c[:i+1:])
        b1 = num
        c1 = a1*b1 +7-i
        print "%d*%d+%d=%d"%(a1,b1,i,c1)
nine1(9)
print '= '*10 +'end nine1'+'= '*10
print '= '*20
print '= '*10 +'start 1111'+'= '*10
def one(num):
    s = '1'*num
    for i in range(num+1):
        a = int(s[:i+1:])
        sums = a*a
        print "%d*%d=%d"%(a,a,sums)
one(9)
print '= '*10 +'end 1111'+'= '*10
