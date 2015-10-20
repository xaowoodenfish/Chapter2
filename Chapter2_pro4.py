__author__ = 'leoxuan'
# Time Oct.20 2015
# The odd of multiplication
def Omul(one,two):
    num = 0
    while two >0:
        if two%2 ==1:
            num = num +one
            one = one*2
            two = two/2
        else:
            two = two/2
            one =one*2
    print "The multiplication A and B is %d."%num
def smd():
    a = raw_input("please input two integer number A and B:")
    Da = []
    Da = a.split(',')
    Omul(int(Da[0]),int(Da[1]))
smd()
print 'whether calculate other multilication,choice Y/N:'
b =raw_input('Your chocie:')
if b =='Y':
    smd()
else:
    print 'Thank you for using!'
