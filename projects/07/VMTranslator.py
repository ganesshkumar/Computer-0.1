#/usr/bin/python

import sys
from Parser import Parser
from Coder import Coder

if len(sys.argv) < 3:
    print 'Please enter input and output filenames'
    sys.exit(1)
else:
    input_files = sys.argv[1:len(sys.argv)-1]
    output_file = sys.argv[len(sys.argv)-1:]

coder = Coder(output_file[0])

for input_file in input_files:
    coder.set_filename(input_file)
    parser = Parser(input_file)
    while(parser.has_more_commands()):
        parser.advance()
        command_type = parser.command_type()
        if command_type == 'C_PUSH' or command_type == 'C_POP':
            coder.write_push_pop(command_type, parser.arg1(), int(parser.arg2()))
        if command_type == 'C_ARITHMETIC':
            coder.write_arithmetic(parser.arg1())