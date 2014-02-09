// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Lazy hacking. Will optimize later. Too excited to see the output right now.


(CHKLOOP)
// Setting 8192(total memory mapped the screen) to R0
@8191
D=A
@R0
M=D
// Check the memory that has been mapped to keyboard
@24576
D=M
@BLACKSCREEN
D;JNE
@WHITESCREEN
D;JEQ
@CHKLOOP
0;JMP

(WHITESCREEN)
@R2
D=M
@CHKLOOP
D;JEQ
(WSLOOP)
@R0
D=M
@CHKLOOP
D;JLT
@16384
D=A
@R0
D=D+M
A=D
D=0
M=D
@R0
M=M-1
@WSLOOP
0;JMP
@R2
M=0
@CHKLOOP
D;JLT


(BLACKSCREEN)
@R2
D=M
@CHKLOOP
D;JNE
(BSLOOP)
@R0
D=M
@CHKLOOP
D;JLT
@16384
D=A
@R0
D=D+M
A=D
D=-1
M=D
@R0
M=M-1
@BSLOOP
0;JMP
@R2
M=-1
@CHKLOOP
0;JMP