from re import A


ORD_A = ord('a')
def lower_ord(c):
    return ord(c) - ORD_A

def count_anagram_substrings(T, S):

        
    m,n,k=len(T),len(S),len(S[0])
    f=[0]*26
    D={}
    for i in range(m):
        f[lower_ord(T[i])]+=1
        if i> k-1:
            f[lower_ord(T[i-k])]-=1
        if i>= k-1:
            key=tuple(f)
            if key in D:
                D[key]+=1
            else:
                D[key]=1 
    A=[0]*n
    for i in range(n):
        f=[0]*26
        for z  in S[i]:
            f[lower_ord(z)]+=1
        key=tuple(f)
        if key in D:
            A[i]=D[key]


    return tuple(A)
