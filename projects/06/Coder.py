#!/usr/bin/python

class Coder:
    def __init__(self):
        pass

    def dest(self, d):
        if d == 'null':
            return '000'
        elif d == 'M':
            return '001'
        elif d == 'D':
            return '010'
        elif d == 'MD':
            return '011'
        elif d == 'A':
            return '100'
        elif d == 'AM':
            return '101'
        elif d == 'AD':
            return '110'
        else:
            return '111'

    def jump(self, j): 
        if j == 'null':
            return '000'
        elif j == 'JGT':
            return '001'
        elif j == 'JEQ':
            return '010'
        elif j == 'JGE':
            return '011'
        elif j == 'JLT':
            return '100'
        elif j == 'JNE':
            return '101'
        elif j == 'JLE':
            return '110'
        else:
            return '111'

    def comp(self, c):
        if c == '0':
            return '0101010'
        elif c == '1':
            return '0111111'
        elif c == '-1':
            return '0111010'
        elif c == 'D':
            return '0001100'
        elif c == 'A':
            return '0110000'
        elif c == '!D':
            return '0001101'
        elif c == '!A':
            return '0110001'
        elif c == '-D':
            return '0001111'
        elif c == '-A':
            return '0110011'
        elif c == 'D+1':
            return '0011111'
        elif c == 'A+1':
            return '0110111'
        elif c == 'D-1':
            return '0001110'
        elif c == 'A-1':
            return '0110010'
        elif c == 'D+A':
            return '0000010'
        elif c == 'D-A':
            return '0010011'
        elif c == 'A-D':
            return '0000111'
        elif c == 'D&A':
            return '0000000'
        elif c == 'D|A':
            return '0010101'
        elif c == 'M':
            return '1110000'
        elif c == '!M':
            return '1110001'
        elif c == '-M':
            return '1110011'
        elif c == 'M+1':
            return '1110111'
        elif c == 'M-1':
            return '1110010'
        elif c == 'D+M':
            return '1000010'
        elif c == 'D-M':
            return '1010011'
        elif c == 'M-D':
            return '1000111'
        elif c == 'D&M':
            return '1000000'
        elif c == 'D|M':
            return '1010101'
        else:
            return ' ' + c + ' '
    def a_address(self, addr):
        return "{0:015b}".format(addr)
