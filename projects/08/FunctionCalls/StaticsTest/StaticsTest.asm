@256
D=A
@SP
M=D
@RETURN..1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(RETURN..1)
(Assembler.THEEND)
@Assembler.THEEND
0;JMP
(Sys.init)
@0
D=A
@R13
M=D
(Sys.init.init.start)
@R13
D=M
@Sys.init.init.end
D; JEQ
D=0
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Sys.init.init.start
0;JMP
(Sys.init.init.end)
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
@RETURN.Sys.init.2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(RETURN.Sys.init.2)
@SP
AM=M-1
D=M
@internal1
M=D
@5
D=A
@0
D=D+A
@internal2
M=D
@internal1
D=M
@internal2
A=M
M=D
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
@RETURN.Sys.init.3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(RETURN.Sys.init.3)
@SP
AM=M-1
D=M
@internal1
M=D
@5
D=A
@0
D=D+A
@internal2
M=D
@internal1
D=M
@internal2
A=M
M=D
@RETURN.Sys.init.4
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(RETURN.Sys.init.4)
@RETURN.Sys.init.5
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(RETURN.Sys.init.5)
(Sys.init.WHILE)
@Sys.init.WHILE
0;JMP
(Class1.set)
@0
D=A
@R13
M=D
(Class1.set.init.start)
@R13
D=M
@Class1.set.init.end
D; JEQ
D=0
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Class1.set.init.start
0;JMP
(Class1.set.init.end)
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@internal1
M=D
@Class1.0
D=A
@internal2
M=D
@internal1
D=M
@internal2
A=M
M=D
@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@internal1
M=D
@Class1.1
D=A
@internal2
M=D
@internal1
D=M
@internal2
A=M
M=D
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@FRAME
AM=M-1
D=M
@THAT
M=D
@FRAME
AM=M-1
D=M
@THIS
M=D
@FRAME
AM=M-1
D=M
@ARG
M=D
@FRAME
AM=M-1
D=M
@LCL
M=D
@RET
A=M
0;JMP
(Class1.get)
@0
D=A
@R13
M=D
(Class1.get.init.start)
@R13
D=M
@Class1.get.init.end
D; JEQ
D=0
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Class1.get.init.start
0;JMP
(Class1.get.init.end)
@Class1.0
D=A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@Class1.1
D=A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@FRAME
AM=M-1
D=M
@THAT
M=D
@FRAME
AM=M-1
D=M
@THIS
M=D
@FRAME
AM=M-1
D=M
@ARG
M=D
@FRAME
AM=M-1
D=M
@LCL
M=D
@RET
A=M
0;JMP
(Class2.set)
@0
D=A
@R13
M=D
(Class2.set.init.start)
@R13
D=M
@Class2.set.init.end
D; JEQ
D=0
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Class2.set.init.start
0;JMP
(Class2.set.init.end)
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@internal1
M=D
@Class2.0
D=A
@internal2
M=D
@internal1
D=M
@internal2
A=M
M=D
@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@internal1
M=D
@Class2.1
D=A
@internal2
M=D
@internal1
D=M
@internal2
A=M
M=D
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@FRAME
AM=M-1
D=M
@THAT
M=D
@FRAME
AM=M-1
D=M
@THIS
M=D
@FRAME
AM=M-1
D=M
@ARG
M=D
@FRAME
AM=M-1
D=M
@LCL
M=D
@RET
A=M
0;JMP
(Class2.get)
@0
D=A
@R13
M=D
(Class2.get.init.start)
@R13
D=M
@Class2.get.init.end
D; JEQ
D=0
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Class2.get.init.start
0;JMP
(Class2.get.init.end)
@Class2.0
D=A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@Class2.1
D=A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@FRAME
AM=M-1
D=M
@THAT
M=D
@FRAME
AM=M-1
D=M
@THIS
M=D
@FRAME
AM=M-1
D=M
@ARG
M=D
@FRAME
AM=M-1
D=M
@LCL
M=D
@RET
A=M
0;JMP