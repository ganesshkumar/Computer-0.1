#/usr/bin/python

import sys
from Parser import Parser
from Coder import Coder

if len(sys.argv) < 3:
    print 'Please enter input and output filenames'
    sys.exit(1)
else:
    input_file =  sys.argv[1]
    output_file = sys.argv[2]

parser = Parser(input_file)
coder = Coder(input_file, output_file)

while(parser.has_more_commands()):
    parser.advance()
    command_type = parser.command_type()
    if command_type == 'C_PUSH' or command_type == 'C_POP':
        coder.write_push_pop(command_type, parser.arg1(), int(parser.arg2()))
    if command_type == 'C_ARITHMETIC':
        coder.write_arithmetic(parser.arg1())
