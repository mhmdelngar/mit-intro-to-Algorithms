from re import L, M
from typing import List, Tuple

def handleCases(B,n1,s1,t1, n2,s2,t2,B1,B2,i,j):
    if t1==t2:
        if s2 !=s1:
            B.append((n1,s1,s2),)
        B.append((n1+n2,s2,t2),)
        i[0]=i[0]+1
        j[0]=j[0]+1
    elif t1<s2:
        B.append((n1,s1,t1),)
        i[0]=i[0]+1  
    elif t1>s2 and t1<t2:
        if(s1!=s2):
            B.append((n1,s1,s2),)
        B.append((n1+n2,s2,t1),)
        z=list(B2[j[0]])
        z[1]=t1
        B2[j[0]]=tuple(z)
        # B2[j]= (z[0],z[1],z[2])
        i[0]=i[0]+1
    elif t1 >t2:
        if(s1!=s2):
            B.append((n1,s1,s2),)
        B.append((n1+n2,s2,t2),)
        z=list(B1[i[0]])     
        z[1]=t2
        B1[i[0]]=tuple(z)
        B1[i[0]]=(z[0],z[1],z[2])
        j[0]=j[0]+1
    elif t1==s2 :
        if n1==n2 and (i ==len(B1) or j ==len(B2)):
            B.append((n1,s1,t2),)
            j[0]=j[0]+1
            i[0]=i[0]+1
            return                
        B.append((n1,s1,t1),)
        i[0]=i[0]+1



def merge(B1 ,B2):
    i=[0]
    j=[0]
    B=[]
    B1=list(B1)
    B2=list(B2)

    while(i[0]+j[0] != len(B1)+ len(B2)):
        print (B1)

        if i[0]+1> len(B1)  :
            # the remainning only in B2
            B.append(tuple(B2[j[0]]),)
            j[0]=j[0]+1
            continue
        elif  j[0]+1>len (B2):
            # the remainning only in B1
            B.append(tuple(B1[i[0]]),)
            i[0]=i[0]+1
            continue
        else:
            
            n1,s1,t1=B1[i[0]]
            n2,s2,t2=B2[j[0]]
        if(s1<s2):
            handleCases(B,n1,s1,t1,n2,s2,t2,B1,B2,i,j)  
        else:
            handleCases(B,n2,s2,t2,n1,s1,t1,B2,B1,j,i)       
    B_ = [B[0]] # remove adjacent with same rooms
    for k, s, t in B[1:]:
        k_, s_, t_ = B_[-1]
        if (k == k_) and (t_ == s):
            B_.pop()
            s = s_
        B_.append((k, s, t))

    return B_



    n1, n2, i1, i2 = len(B1), len(B2), 0, 0
    x = 0 # invariant: t < min(t1, t2)
    B = [] # invariant: B is satisfying booking up to time x
    while i1 + i2 < n1 + n2:
        if i1 < n1: k1, s1, t1 = B1[i1]
        if i2 < n2: k2, s2, t2 = B2[i2]
        if i2 == n2: # only bookings in B1 remain
            k, s, x = k1, max(x, s1), t1
            i1 += 1
        elif i1 == n1: # only bookings in B2 remain
          k, s, x = k2, max(x, s2), t2
          i2 += 1
        else: # bookings remain in B1 and B2
            if x < min(s1, s2): # shift x to start of first booking
                x = min(s1, s2)


def satisfying_booking(R):
    if len(R)==1:
        s, t = R[0]
        return[(1,s,t),]
    m = len(R) // 2
    R1, R2 = R[:m], R[m:] 
    B1 = satisfying_booking(R1) 
    B2 = satisfying_booking(R2)
    B=merge(B1, B2) 

    return tuple(B)
