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

//Read R0 to D
@R0
D=M

@END
D; JLE

(LOOP)
@R2
D=M

@R1
D=D+M
@R2
M=D

@R0
M=M-1
D=M

@LOOP
D;JGT

// infinite loop
(END)
@END
0;JMP
