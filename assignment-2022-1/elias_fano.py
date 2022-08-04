import hashlib
import math
import sys
def get_Data():
    list_of_numbers=[]
    with open(sys.argv[1],encoding='utf8') as f:
        lines=f.readlines()
    for i in lines:
        list_of_numbers.append(int(i))
    l= math.floor((math.log2(max(list_of_numbers)/len(list_of_numbers))))# the l which is rounded down(last bits to exctract)
    size=len(list_of_numbers)*math.floor((math.log2(max(list_of_numbers)/len(list_of_numbers))))# The size of L 
    L_size=math.ceil(size/8)
    U_size=math.ceil((len(list_of_numbers)+max(list_of_numbers)/2**l)/8)
    first_bits=math.ceil((math.log2(max(list_of_numbers))-l)) # the number of first bits to be extracted
    L=create_L(l,L_size,list_of_numbers)
    U=create_U(l,first_bits,list_of_numbers,U_size)
    Output(L,U,l)

def create_L(l,L_size,list_of_numbers):
    bit_format1=(1<<l)-1
    count,k=0,8
    L=bytearray(L_size) 
    for i in list_of_numbers:
            if k-l>=0: # k=8,5,2
                k-=l
                end_bits=i & bit_format1 # 3 last bits
                L[count]+=end_bits<<k
            else:
                bit_formatk=(1<<k)-1 # vriski posa teleftaia theloume e.g 2
                p=i>>l-k # petaei gia na 
                end_bits= p & bit_formatk 
                L[count]+=end_bits<<0
                rest=l-k
                k=8
                count+=1
                bit_formatk=(1<<rest)-1
                end_bits=i & bit_formatk
                L[count]+=end_bits<<k-rest
                k-=rest
    return L
    
def create_U(l,first_bits,list_of_numbers,U_size):
    U=bytearray(U_size)
    bit_format1=(1<<first_bits)-1
    for i in range(len(list_of_numbers)):
        remove=list_of_numbers[i]>>l
        bit= remove & bit_format1
        push_position=i+bit
        mod=push_position%8
        div=push_position//8
        if mod==0:
            U[div]+=1<<7
        else:
            U[div]+=1<<7-mod
    return U

def Output(L,U,l):       
    print("l",l)
    print("L")
    for i in L:
        print(format(i,'08b')) # print in 8 bit format
    print("U")
    for i in U:
        print(format(i,'08b')) # print in 8 bit format
    #SHA-256
    m = hashlib.sha256()
    m.update(L)
    m.update(U)
    digest = m.hexdigest()
    print(digest)  

get_Data()#begin the execution
