# Sorted Integers Compression & Decompression

## Introduction

In this project we are trying to effectively compress a list of non-decreasing integers by using Elias-Fano encoding. This type of compression uses a sussinct data-structure which means that the encoding space requirement is very close to the theoretical lower bound.<br><br>
The analytical implementation of this algorithm is described [here](https://github.com/Philippos01/Algorithms-Data-Structures/blob/main/assignment-2022-1/assignment-2022-1.pdf)

## Run the program

You can run the program by the following command:
```
python elias_fano.py file
```

## Output

After running the program, it will compress the data and print the variables ```l,L,M,digest``` in the following state:
``` 
l-> number
L->bytearray
U->bytearray
digest-> A unique 256-bit hash for the compression
```

## Author 
[Philippos Priovolos](https://github.com/Philippos01)
