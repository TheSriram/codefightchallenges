def findRange(array, n):
    sum_found = False
    for startpoint in range(0, len(array)):
        sum = 0
        for elem in array[startpoint:]:
            sum = sum + elem
            if sum == n:
                sum_found = True
                return True
                
    if sum_found == False:
        return False
