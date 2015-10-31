def recurseme(xa, xb, ya, yb, m ,n, count):
    if xa + xb > m or ya + yb > n:
        return -1
    if (xa + xb) == m and (ya + yb) == n:
        return count
    val1 = recurseme(xa + xb, ya + yb, ya, yb, m ,n, count+1)
    if val1 >= 0:
        return val1
    val2 = recurseme(xa, ya, xa + xb, ya + yb, m ,n, count+1)
    if val2 >= 0:
        return val2
    return -1

def NumberGameIV(m, n):
    xa, ya = (1,0)
    xb, yb = (0,1)
    return recurseme(xa, xb, ya, yb, m, n, 0)
