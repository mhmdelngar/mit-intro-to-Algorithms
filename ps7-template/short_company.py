def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    c = C[0]
    S = []
    ##################
    # YOUR CODE HERE #
    ##################
    par=[[(0,0) for _ in range(0,n*k)] for _ in range(0,len(P))]
    x=[[0 for _ in range(0,n*k)] for _ in range(0,len(P))]
    lisOfMax=[(0,0) for _ in range(0,len(C))]
    for i in range(0,len(C)):
        maximum=0
        maxIndex=0
        for j in reversed(range(0,len(P[i]))):
            best=0
            for m in range(j+1,min(j+1 + (k - 1) - (j % k) + k, n*k - 1)):
                if P[i][j]>P[i][m]:
                    if x[i][m]>best:

                        best=x[i][m]
                        par[i][j]=(i,m)
            x[i][j]=1+best
            if x[i][j]>maximum:
                maximum=x[i][j]
                maxIndex=j
        lisOfMax[i]=(maximum,maxIndex)        
    max=0
    for s in range(0,len(C)):     
        if lisOfMax[max][0]<lisOfMax[s][0]:
            max=s
            
    c=C[max]
    g= par[max][lisOfMax[max][1]]
    S.append(P[max][lisOfMax[max][1]])
    while par[g[0]][g[1]]!=(0,0):
        S.append(P[g[0]][g[1]])
        g= par[g[0]][g[1]]
        
    S.append(P[g[0]][g[1]])

    return (c, S)
