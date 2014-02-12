#!/usr/bin/python

import sys

from Parser import Parser
from Coder import Coder
from SymbolTable import SymbolTable

coder = Coder()
stable = SymbolTable()
asm_file = None

if len(sys.argv) is 0:
    print 'Please enter a filename as argument'
    sys.exit(1)
else:
    asm_file =  sys.argv[1]

# PASS 1
RAM_top = 16
pc = 0
parser = Parser(asm_file)
while parser.has_more_commands():
    pc += 1
    parser.advance()
    command_type = parser.command_type()
    if command_type == 'A_COMMAND':
        symbol = parser.symbol()
        if not stable.contains(symbol):
            stable.add_entry(symbol, RAM_top)
            RAM_top += 1
    elif command_type == 'L_COMMAND':
        pc -= 1
        symbol = parser.symbol()
        stable.add_entry(symbol, pc)

# PASS 2 
parser = Parser(asm_file)
while parser.has_more_commands():
    parser.advance()
    command_type = parser.command_type()
    if command_type == 'A_COMMAND':
        symbol = parser.symbol()
        if symbol.isdigit():
            print "0" + str(coder.a_address(int(symbol)))
        else:
            print "0" + str(coder.a_address(stable.get_address(symbol)))
    elif command_type == 'C_COMMAND':
        print "111" + coder.comp(parser.comp()) + coder.dest(parser.dest()) + coder.jump(parser.jump())
