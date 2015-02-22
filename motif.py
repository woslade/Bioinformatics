def motif(s,t):
    '''
    Assume t <= s. Given two strings s and t, t is a substring of s if t is contained
    as a contiguous collection of symbols in s. A substring of s can be represented
    as s[j:k], where j and k represent the starting and ending positions of the 
    substring in s; for example, if s = 'AUGCUUCAGAAAGGUCUUACG', then s[2:5] = "UGCU"
    Input
    ---
    s: string
    t: substring
    
    Ouput
    ---
    return location
    '''
    location = ''

    for num in range(len(s)):
        if s[num:].startswith(t):
            location += str(num+1) + ' ' ## num + 1 because python starts at 0, not 1
    return location
