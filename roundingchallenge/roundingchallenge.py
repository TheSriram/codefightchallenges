def rounding(n, m):
    multiple = float(n)/float(m)
    float_round = multiple - int(multiple)
    if float_round < 0.5:
        return int(multiple) * m
    elif float_round > 0.5:
        return (int(multiple) + 1) * m
    else:
        return n
