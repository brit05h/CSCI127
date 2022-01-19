
#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 19,2020
#this program writes a simplified machine language program

ADDI $sp, $sp, -12
ADDI $t0, $zero, 73 # I
SB $t0, 0($sp)
ADDI $t0, $zero, 32 # (space)
SB $t0, 1($sp)
ADDI $t0, $zero, 108 # l
SB $t0, $zero, 111 # o
SB $t0, 3($sp)
ADDI $t0, $zero, 118 # v
SB $t0, 4($sp)
ADDI $t0, $zero, 101 # e
SB $t0, 5($sp)
ADDI $t0, $zero, 32 # (space)
SB $t0, 6($sp)
ADDI $t0, $zero, 77 # M
SB $t0, 7($sp)
ADDI $t0, $zero, 73 # I
SB $t0, 8($sp)
ADDI $t0, zero, 80 # P
SB $t0, 9($sp)
ADDI $t0, $zero, 83 # S
SB $t0, 10($sp)
ADDI $t0, $Zero, 33 # !
SB $t0, 11($sp)
ADDI $v0, $zero, 4 # 4 is for print string
ADDI $a0, $sp, 0

syscall #print to the log
