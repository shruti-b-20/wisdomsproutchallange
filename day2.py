def missing_no(arr):
    n=len(arr)
    total=n*(n-1)//2
    actual=total(arr)
    return total-actual