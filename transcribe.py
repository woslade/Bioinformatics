def transcribe(t):
    """
    An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', 
    and 'U'. Given a DNA string t corresponding to a coding strand, its 
    transcribed RNA string u is formed by replacing all occurrences of 'T' in t 
    with 'U' in u.
    
    Input
    ---
    t: A DNA string t having length at most 1000 nt
    
    Ouput
    ---
    return the transcribed RNA string of t
    """
    
    RNA = ''
    
    for nt in t:
        if nt == "T":
            RNA += 'U'
        elif nt == "A" or nt == "C" or nt == "G":
            RNA += nt
        else:
            return "Not a nucleotide!"
    return RNA
