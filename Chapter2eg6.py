# time 10.20 2015
# if not input a int ,return a tip to back until a right in
a = raw_input('Input an integer:')
while True:
    if not a.isdigit():
        print 'Error: try again.'
        a = raw_input('Input an integer:')
    else:
        print 'The integer is:%s'%a
        break
