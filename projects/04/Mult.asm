// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[3], respectively.)

// Put your code here.

// Setting R2 to zero
@0
D=A

@R2
M=D

// Read R0 to D
@R0
D=M

// If R0 is zero go to infinite loop
@END
D; JLE

(LOOP)
// Read sum
@R2
D=M

// Add R1 to sum
@R1
D=D+M
@R2
M=D

// Decrement R0
@R0
M=M-1
D=M

@LOOP
D;JGT

// infinite loop
(END)
@END
0;JMP
