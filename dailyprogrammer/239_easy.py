n = input()

while n != 1:
    x = n % 3
    
    if x == 0:
        print '%d 0' % n
    elif x == 1:
        print '%d -1' % n
        n -= 1
    else:
        print '%d 1' % n
        n += 1

    n /= 3

print '1'