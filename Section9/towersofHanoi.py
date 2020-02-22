def move(a,b):
    print("{} moves to {}".format(a, b))


def fooMoov(f, v, t):
    move(f, v)
    move(v, t)


def hanoi(n,f,h,t):
    if n == 0:
        pass

    # n : Number of Disks
    # f : From position
    # h : helper position
    # t : too position
    else:
        hanoi(n-1, f, t, h)
        move(f, t)
        hanoi(n - 1, h, f, t)

hanoi(4,"A", "B", "C")