def climb_stairs(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        return climb_stairs(n-1)+climb_stairs(n-2)
n=2
climb_stairs(n)