def NumberGameIII(S):
    flag_max = True
    min_number = min(S)
    for elem in S:
        quotient = float(elem)/float(min_number)
        flag = quotient - int(quotient)
        if flag != 0.0:
            flag_max = False
            
    if flag_max:
        return min_number
    else:
        return -1
