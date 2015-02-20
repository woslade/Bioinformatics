def baseCount(s):
    """
    Rosalind: Counting DNA nucleotides
    Input
    ---
    s: a DNA string of at most 1000 nucleotides
    
    Output
    ---
    Four integers (separated by spaces) counting the respective number of times 
    that the symbols 'A', 'C', 'G', and 'T' occur in s.
    """
    A = ""
    C = ""
    G = ""
    T = ""
     
    for nt in s:
        if nt == 'A':
            A += nt
        elif nt == 'C':
            C += nt
        elif nt == 'G':
            G += nt
        elif nt == 'T':
            T += nt
        else:
            return "Not a nucleotide!"
            
    return "%s %s %s %s" %(len(A), len(C), len(G), len(T))
