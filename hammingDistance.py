def pointMutations(s,t):
    '''
    Assume len(s) == len(t)
    Assume len(s) <= 1kbp
    Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of 
    corresponding symbols that differ in s and t.
    
    Input
    ---
    s: string
    t: string
    
    Ouput
    ---
    return Hamming distance dH(s,t)
    '''
    distance = 0
    
    for num in range(len(s)):
        if s[num] != t[num]:
            distance += 1
    return distance
