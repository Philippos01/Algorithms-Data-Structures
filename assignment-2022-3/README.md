# Cycle Detection in a sequence of numbers

## Introduction

In this project we are trying to detect cycles in sequence of numbers. This implementation is very useful in various scientific subjects like cryptography. For example, in Diffie-Hellman method for key exhanging the security is based in the problem of the discrete logarithm. This problem is about finding the variable x in functions like $f(x)=𝑔^x mod p$ which are periodic functions and the only possible way to find this number is by examining every number of the period. So this algorithm implementation is of a high importance since it can help examine and find secure pairs of numbers that have very large period and cannot be cracked with brute-force.<br>
The algorithm that we use is an optimal variation of the Robert W. Floyd algorithm that examines only b numbers in a $g*b$ distance.

## Run the program

You can run the program by the following command:
```
python cycle_detection [-t] b g table_size input_sequence
```
The meaning of each of the main parameters is:
* b-> a possitive integer
* g-> a possitive integer
* table_size-> the max_size that is given to the algorithm

For the analytical explanation of the parameter ```t``` take a look [here](https://github.com/Philippos01/Algorithms-Data-Structures/blob/main/assignment-2022-2/assignment-2022-3.pdf) in page 9.

## Output

After running the programm, the 1st element and the length of the cycle will be printed in the following format:<br><br>
<b>Example<b>
 ```
  cycle 6 leader 4
  ```

 ## Author 
[Philippos Priovolos](https://github.com/Philippos01)
