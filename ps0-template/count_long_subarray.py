def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    
    min=A[0]
    max=A[1]
    leng=0
    m=0
    z=len(A)
    maxM=0
    for i in range (z):
        min=A[i]
        if(i+1<z):
            max=A[i+1]
        if(min<max):
            m=m+1
        else :

            if(m>maxM):
                maxM=m
                leng=1
            elif m==maxM:
                leng=leng+1
                
            m=0    
    return leng         
