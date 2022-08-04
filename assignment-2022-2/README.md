# Sequence Alignment

## Introduction

In this project we are trying to align string sequences optimally by using two different techniques. The first technique is an algorithm produced by Needleman–Wunsch
for the purpose of aligning protein and nucleotide sequences in bioinformatics. This algorithm gives a score to each possible alignment and then it compares it chooses allignment or the alignments with the highest score. The second technique that is used is the Hirschberg's algorithm. This algorithm produces the same results as the
Needleman–Wunsch algorithm but in a more space-efficient way by using the divide and conquer method. Specifically it uses recursion for both 2 alignments until each alignment is over or both alignments have length 1. 

## Run the program

You can run the program by the following command:
```
python hirschberg.py [-t] [-f] [-l] gap match differ a b
```
The meaning of each of the main parameters is:
* gap -> it is the ```g``` parameter that is substracted from the alignment score when we remove an element.
* match -> it is the ```m``` parameter that is added to the score when the two elements of the alignments are the same.
* differ -> it is the ```d``` parameter that is substracted from the alignment score when the two elements of the alignments are different.

For the analytical explanation of the parameters ```t,f,l``` take a look [here](https://github.com/Philippos01/Algorithms-Data-Structures/blob/main/assignment-2022-2/assignment-2022-2.pdf) in page 9.

## Output

After running the programm, all the possible alligned sequences will be printed in the following format:<br><br>
<b>Example<b>
 ``` 
 GAC-G-C-
-ACTGACG
  
---GACGC
ACTGACG-
```


## Author 
[Philippos Priovolos](https://github.com/Philippos01)


