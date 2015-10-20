# Time Oct.20 2015
# The height of the folded paper
def hei(times):
    for i in range(1,times):
        paper = 1.0/120
        tims = 2**i
        paper *=tims
        if 10**5>paper>10**2:
            print 'this %d fold will be %f m. '%(i,paper/10**2)
        elif 10**5<paper:
            print 'this %d fold will be %f Km. '%(i,paper/10**5)
        else:
             print 'this %d fold will be %f cm. '%(i,paper)
hei(30)