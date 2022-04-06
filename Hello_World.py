print('Hello World')
n = float(input('Enter the number\n'))
print('Entered Number is', n)
temp = n % 0.0002
if n % 0.0002 != 0:
    print('Result to above mod operation is %f' % temp)
    print('Number enter %3.3f is odd' % n)
else:
    print('Number enter is even')


