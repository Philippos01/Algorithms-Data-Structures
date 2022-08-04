import math
import sys
if sys.argv[1]=="-t":
    if sys.argv[2]=="-f":
        flag=1# -t kai -f 
        g=int(sys.argv[4])
        m=int(sys.argv[5])
        d=-int(sys.argv[6])
        with open(sys.argv[7]) as f:
            A=f.readlines()
        with open(sys.argv[8]) as p:
            B=p.readlines()
    else:
        flag=2# -t kai g 
        g=int(sys.argv[2])
        m=int(sys.argv[3])
        d=-int(sys.argv[4])
        A=sys.argv[5]
        B=sys.argv[6]
elif sys.argv[1]=="-f":
        flag=3# -f kai g
        g=int(sys.argv[3])
        m=int(sys.argv[4])
        d=-int(sys.argv[5])
        with open(sys.argv[6]) as f:
            A=f.readlines()
            #print(A)
        with open(sys.argv[7]) as p:
            B=p.readlines()
else:
        flag=4# mono g
        g=int(sys.argv[1])
        m=int(sys.argv[2])
        d=-int(sys.argv[3])
        A=sys.argv[4]
        B=sys.argv[5]

def NeedlemanWunsch(A,B):
    WW,ZZ=[],[]
    W,Z="",""
    F=Construct_F(A,B)
    EnumerateAlignments(A,B,F,W,Z,WW,ZZ)
    return WW,ZZ


def Construct_F(A,B):
    F=[[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(len(A)+1):
        F[i][0]=g*i
    for j in range(len(B)+1):
        F[0][j]=g*j
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if i==0 or j==0:
                continue
            if A[i-1]==B[j-1]:
                F1=F[i-1][j-1]+m
            else:
                F1=F[i-1][j-1]-d
            F2=F[i-1][j]+g
            F3=F[i][j-1]+g
            F[i][j]=max(F1,F2,F3)
    return F
    

def EnumerateAlignments(A,B,F,W,Z,WW,ZZ):
    i=len(A)
    j=len(B)
    if i==0 and j==0:
        WW.append(W)
        ZZ.append(Z) 
        return 
    if i>0 and j>0:
        m=Compare(A[i-1],B[j-1])
        if F[i][j]==F[i-1][j-1]+m:
             EnumerateAlignments(A[0:i-1],B[0:j-1],F,A[i-1]+W,B[j-1]+Z,WW,ZZ)
    if i>0 and F[i][j]==F[i-1][j]+g:
         EnumerateAlignments(A[0:i-1],B,F,A[i-1]+W,"-"+Z,WW,ZZ)
    if j>0 and F[i][j]==F[i][j-1]+g:
          EnumerateAlignments(A,B[0:j-1],F,"-"+W,B[j-1]+Z,WW,ZZ)
    
def Compare(a,b):
    if a==b:
        return m
    else:
        return -d

def ComputeAlignmentScore(A,B):
    L=[0]*(len(B)+1)
    for j in range(0,len(B)+1):
            L[j]=(j*g)
    for i in range(1,len(A)+1):
        K=L.copy()
        L[0]=i*g
        for j in range(1,len(B)+1):
            m=Compare(A[i-1],B[j-1])
            L[j]=max(L[j-1]+g,K[j]+g,K[j-1]+m)
    return L

def UpdateAlignments(WW,ZZ,WWlr,ZZlr,WWl,ZZl,WWr,ZZr):
    w,z=[],[]
    if len(WWlr)==2:
            new=""
            for x in WWlr:
                if type(x)==list:
                    new+=x[0]
                else:
                    new+=x
            WW.append(new)
    else:#len>2
        if len(WWl)==2 and len(WWr)==1:
            new=""
            new1=""
            new+=WWlr[0]+WWlr[2]
            new1+=WWlr[1]+WWlr[2]
            WW.append(new)
            WW.append(new1)
        elif len(WWr)==2 and len(WWl)==1:
            new=""
            new1=""
            new+=WWlr[0]+WWlr[1]
            new1+=WWlr[0]+WWlr[2]
            WW.append(new)
            WW.append(new1)  
        elif len(WWl)==2 and len(WWr)==2:
            new=""
            new+=WWlr[0]+WWlr[2]
            WW.append(new)         
    if len(ZZlr)==2:
            new1=""
            for l in ZZlr:
                new1+=l
            ZZ.append(new1)
    else:#len>2
        if len(ZZl)==2 and len(ZZr)==1:
            new=""
            new1=""
            new+=ZZlr[0]+ZZlr[2]
            new1+=ZZlr[1]+ZZlr[2]
            ZZ.append(new)
            ZZ.append(new1)
        elif len(ZZr)==2 and len(ZZl)==1:
            new=""
            new1=""
            new+=ZZlr[0]+ZZlr[1]
            new1+=ZZlr[0]+ZZlr[2]
            ZZ.append(new)
            ZZ.append(new1)  
        elif len(ZZl)>1 and len(ZZr)>1:
            new=""
            new+=ZZr[0]+ZZlr[2]
            ZZ.append(new) 
    p=[]
    length=[]
    for i in range(len(WW)):
        length.append(len(WW[i]))
        p.append(WW[i]+ZZ[i])
    a_set=set(p)
    if len(p) != len(a_set):
        p=list(dict.fromkeys(p))
        for m,i in enumerate(p):
            w.append(i[:length[m]])
            z.append(i[length[m]:])
        WW=w
        ZZ=z
    return WW,ZZ    
        
def Max_Value(S):
    m=max(S)
    indexes=[index for index, value in enumerate(S) if value == m]
    return indexes
    
def Hirschberg(A,B):
    if len(A)==0:
        WW=["-"*len(B)]
        ZZ=[B]
    elif len(B)==0:
        WW=[A]
        ZZ=["-"*len(A)]
    elif len(A)==1 or len(B)==1:
        (WW,ZZ)=NeedlemanWunsch(A,B)
    else:
        i=math.floor(len(A)/2)
        Sl=ComputeAlignmentScore(A[:i],B)
        Sr=ComputeAlignmentScore(A[i:][::-1],B[::-1])
        S = [sum(i) for i in zip(Sl, Sr[::-1])]
        J=Max_Value(S)
        WW,ZZ=[],[]
        for j in J:
            if flag==1 or flag==2:
                print(i,j)
            if flag==1 or flag==3:
                (WWl,ZZl)=Hirschberg(A[:i],B[:j])
                (WWr,ZZr)=Hirschberg(A[i:],B[j:])
                WW,ZZ=UpdateAlignments(WW,ZZ,WWl+WWr,ZZl+ZZr,WWl,ZZl,WWr,ZZr)
            else:
                (WWl,ZZl)=Hirschberg(A[:i],B[:j])
                (WWr,ZZr)=Hirschberg(A[i:],B[j:])
                WW,ZZ=UpdateAlignments(WW,ZZ,WWl+WWr,ZZl+ZZr,WWl,ZZl,WWr,ZZr)
    return(WW,ZZ)
    
(WW,ZZ)=Hirschberg(A,B)
if flag==1:
  for i in range(len(WW)):
        print(WW[i])
        print(ZZ[i],"\n")
elif flag==2:
    for i in range(len(WW)):
        print(WW[i])
        print(ZZ[i],"\n")
elif flag==3:  
    #print(WW,ZZ)
    WW=WW[0].split("\n")
    ZZ=ZZ[0].split("\n")
    print(WW,ZZ)
    for i in range(len(WW)):
        if WW[i]==ZZ[i]:
            print("= ",WW[i])
            print("= ",ZZ[i])
        elif WW[i]!=ZZ[i]:
            print("< ",WW[i])
            print("> ",ZZ[i])   
else:
    for i in range(len(WW)):
        print(WW[i])
        print(ZZ[i],"\n")