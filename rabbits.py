def fib(n,k):
    """
    Function for fibonacci sequence where n is the number of months and k is the number
    of pairs each mature pair produces after breeding. In this model, rabbits are immortal, 
    as per the original fibonacci sequence.
    
    Input
    ---
    n: integer for months
    k: integer for pairs of rabbits produced by a 
    
    Output
    ---
    return number of rabbit pairs alive after n months
    """
    
    if n == 0:
        return 0
    elif n==1:
        return 1
    else: 
        return fib(n-1,k) + fib(n-2,k)*k
