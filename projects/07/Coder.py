#! /usr/bin/python

class Coder:
    def __init__(self, input_filename, output_filename):
        self.input_file = input_filename
        self.output_file = open(output_filename, 'w+')
        self.has_comparision = False
        self.condition_suffix = 1

    def set_filename(self, filename):
        if self.output_file is not None:
            self.output_file.flush()
            self.output_file.close()
        self.output_file = open(filename, 'w+')

    def write_arithmetic(self, command):
        if command == 'ADD' or command == 'SUB' or command == 'AND' or command == 'OR':
            self.pop()
            print '@SP'
            print 'AM=M-1'
            print 'D=D+M' if command == 'ADD' else 'D=M-D' if command == 'SUB' else 'D=D&M' if command == 'AND' else 'D=D|M'
            self.push()
        elif command == 'NEG':
            print '@SP'
            print 'A=M-1'
            print 'M=-M'
        elif command == 'EQ' or command == 'LT' or command == 'GT':
            suffix = str(self.condition_suffix)
            self.condition_suffix += 1
            self.write_arithmetic('SUB')
            print '@startC' + suffix
            print 'D;JEQ' if command == 'EQ' else 'D;JLT' if command == 'LT' else 'D;JGT'
            self.pop()
            print 'D=0'
            self.push()
            print '@endC' + suffix
            print '0;JMP'
            print '(startC' + suffix + ')'
            self.pop()
            print 'D=-1'
            self.push()
            print '(endC' + suffix + ')'
        elif command == 'NOT':
            self.pop()
            print 'D=!D'
            self.push()


    def write_push_pop(self, command_type, segment, index):
        if command_type == 'C_PUSH':
            self.get_from_memory(segment, index);
            self.push()
        else:
            self.pop()
            self.put_to_memory(segment, index)

    def push(self):
        ''' Puts the value in D register to stack'''
        print '@SP'
        print 'A=M'
        print 'M=D'
        print '@SP'
        print 'M=M+1'

    def pop(self):
        ''' Gets the value in stack to  D register'''
        print '@SP'
        print 'AM=M-1'
        print 'D=M'


    def get_from_memory(self, segment, index):
        ''' Gets the value to D register'''
        if segment == 'constant':
            print '@' + str(index)
            print 'D=A'
        else:
            self.calculate_address(segment, index)
            print 'A=D'
            print 'D=M'

    def put_to_memory(self, segment, index):
        ''' Puts the value in D register to the memory'''
        # Using temp registers R5 and R6
        if segment == 'constant':
            pass
        else:
            print '@internal1'
            print 'M=D'
            self.calculate_address(segment, index)
            print '@internal2'
            print 'M=D'
            print '@internal1'
            print 'D=M'
            print '@internal2'
            print 'A=M'
            print 'M=D'

    def calculate_address(self, segment, index):
        ''' Calculates the effective address using segment and index and puts in D'''
        if segment == 'local':
            print '@LCL'
            print 'D=M'
            print '@' + str(index)
            print 'D=D+A'
        elif segment == 'argument':
            print '@ARG'
            print 'D=M'
            print '@' + str(index)
            print 'D=D+A'
        elif segment ==  'this':
            print '@THIS'
            print 'D=M'
            print '@' + str(index)
            print 'D=D+A'
        elif segment == 'that':
            print '@THAT'
            print 'D=M'
            print '@' + str(index)
            print 'D=D+A'
        elif segment == 'pointer':
            print '@3'
            print 'D=A'
            print '@' + str(index)
            print 'D=D+A'
        elif segment == 'temp':
            print '@5'
            print 'D=A'
            print '@' + str(index)
            print 'D=D+A'
        elif segment == 'static':
            print '@' + self.input_file + '.' + str(index)
            print 'D=A'


