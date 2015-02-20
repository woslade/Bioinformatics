def reverse(s):
    """
    In DNA, symbols "A" and "T" or "C" and "G" are complements. 
    Input
    ---
    s: a DNA string of length at most 1000 bp
    
    Output
    ---
    return: reverse complement of s
    """
    sc = []
    sList = list(s)
    sList.reverse()
    
    
    for bp in sList:
        if bp == "A":
            sc.append("T")
        elif bp == "T":
            sc.append("A")
        elif bp =="C":
            sc.append("G")
        elif bp == "G":
            sc.append("C")
        else:
            return "Not a nucleotide!"
        
    return "".join([x for x in sc])
