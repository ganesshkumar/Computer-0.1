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
coder.set_filename(input_files[0])
coder.write_init()

for input_file in input_files:
    coder.set_filename(input_file)
    parser = Parser(input_file)
    while(parser.has_more_commands()):
        parser.advance()
        command_type = parser.command_type()
        #coder.output_file.write(command_type + ' | ' + parser.current_command + '\n')
        if command_type == 'C_PUSH' or command_type == 'C_POP':
            coder.write_push_pop(command_type, parser.arg1(), int(parser.arg2()))
        elif command_type == 'C_ARITHMETIC':
            coder.write_arithmetic(parser.arg1())
        elif command_type == 'C_LABEL':
            coder.write_label(parser.arg1())
        elif command_type == 'C_GOTO':
            coder.write_goto(parser.arg1())
        elif command_type == 'C_IF':
            coder.write_if(parser.arg1())
        elif command_type == 'C_FUNCTION':
            coder.write_function(parser.arg1(), parser.arg2())
        elif command_type == 'C_RETURN':
            coder.write_return()
        elif command_type == 'C_CALL':
            coder.write_call(parser.arg1(), parser.arg2())