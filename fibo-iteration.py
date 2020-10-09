#Haven't done a good ole Fibonacci in awhile.   I've got the recursive solution memorized, let's do something a lil different.
a, b = 1, 2
while (a<3000):
    if (a > b):
        print b
        b = a + b
    else:
        print a
        a = a + b
