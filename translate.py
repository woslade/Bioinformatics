def translate(s):
    """
    Converts an mRNA string into a protein string. Assumes the mRNA strand starts with a start codon
    and ends with a stop codon.
    Input
    ---
    s: string, mRNA strand.
    
    Output
    ---
    return string, translated protein.
    """
    template = {"UUU" : "F", "UUC" : "F","UUA" : "L","UUG" : "L", "UCU" : "S", "UCC" : "S",
                "UCA" : "S", "UCG" : "S", "UAU" : "Y", "UAC" : "Y", "UAA" : '',"UAG" : '',
                "UGU" : 'C', 'UGC' : 'C','UGA' : '','UGG' : 'W','CUU' : 'L','CUC' : 'L','CUA' : 'L',
                'CUG' : 'L', 'CCU' : 'P', 'CCC' : 'P', 'CCG' : 'P','CAU' : 'H', 'CAC' : 'H', 
                'CAA' : 'Q', 'CAG' : 'Q','CGU' : 'R','CGC' : 'R','CGA' : 'R','CGG' : 'R',
                'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I', 'AUG' : 'M', 'ACU' : 'T', 'ACC' : 'T',
                'ACA' : 'T', 'ACG' : 'T', 'AAU' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K',
                'AGU' : 'K', 'AGU' : 'S', 'AGC' : 'S', 'AGA' : 'R', 'AGG' : 'R', 'GUU' : 'V',
                'GUC' : 'V', 'GUG' : 'V', 'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
                'GAU' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E', 'GGU' : 'G', 'GGC' : 'G', 
                'GGA' : 'G', 'GGG' : 'G', 'CCA' : 'P', 'GUA' : "V"}
    
    count = 0
    protein = ''
    
    for num in range(3, len(s)+3, 3):
        protein += template[s[count:num]]
        count += 3
    return protein
