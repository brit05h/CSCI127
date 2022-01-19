#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 19,2020
#this program writes a simplified machine language program

ADDI $s0, $zero, 0
ADDI $s1, $zero, 100
ADDI $s2, $zero, 500
AGAIN: ADD $s0,$s0,$s1
BEQ $s0, $s2, DONE
J AGAIN
DONE: #to break out of the loop
