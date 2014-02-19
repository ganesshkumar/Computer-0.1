#! /usr/bin/python

class Coder:
    def __init__(self, output_filename):
        self.input_file = ''
        self.output_file = open(output_filename, 'w+')
        self.has_comparision = False
        self.condition_suffix = 1

    def set_filename(self, filename):
        filename = filename.split('.')[0]
        if len(filename.split('/')) > 0: # Linux and Mac
            filename = filename.split('/')[len(filename.split('/'))-1]
        if len(filename.split('\\')) > 0: # Windows
            filename = filename.split('\\')[len(filename.split('\\'))-1]
        self.input_file = filename

    def write_arithmetic(self, command):
        if command == 'ADD' or command == 'SUB' or command == 'AND' or command == 'OR':
            self.pop()
            self.output_file.write('@SP' + '\n')
            self.output_file.write('AM=M-1' + '\n')
            self.output_file.write('D=D+M\n' if command == 'ADD' else 'D=M-D\n' if command == 'SUB' else 'D=D&M\n' if command == 'AND' else 'D=D|M\n')
            self.push()
        elif command == 'NEG':
            self.output_file.write('@SP' + '\n')
            self.output_file.write('A=M-1' + '\n')
            self.output_file.write('M=-M' + '\n')
        elif command == 'EQ' or command == 'LT' or command == 'GT':
            suffix = str(self.condition_suffix)
            self.condition_suffix += 1
            self.write_arithmetic('SUB')
            self.output_file.write('@startC' + suffix + '\n')
            self.output_file.write('D;JEQ\n' if command == 'EQ' else 'D;JLT\n' if command == 'LT' else 'D;JGT\n')
            self.pop()
            self.output_file.write('D=0' + '\n')
            self.push()
            self.output_file.write('@endC' + suffix + '\n')
            self.output_file.write('0;JMP' + '\n')
            self.output_file.write('(startC' + suffix + ')' + '\n')
            self.pop()
            self.output_file.write('D=-1' + '\n')
            self.push()
            self.output_file.write('(endC' + suffix + ')' + '\n')
        elif command == 'NOT':
            self.pop()
            self.output_file.write('D=!D' + '\n')
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
        self.output_file.write('@SP' + '\n')
        self.output_file.write('A=M' + '\n')
        self.output_file.write('M=D' + '\n')
        self.output_file.write('@SP' + '\n')
        self.output_file.write('M=M+1' + '\n')

    def pop(self):
        ''' Gets the value in stack to  D register'''
        self.output_file.write('@SP' + '\n')
        self.output_file.write('AM=M-1' + '\n')
        self.output_file.write('D=M' + '\n')


    def get_from_memory(self, segment, index):
        ''' Gets the value to D register'''
        if segment == 'constant':
            self.output_file.write('@' + str(index) + '\n')
            self.output_file.write('D=A' + '\n')
        else:
            self.calculate_address(segment, index)
            self.output_file.write('A=D' + '\n')
            self.output_file.write('D=M' + '\n')

    def put_to_memory(self, segment, index):
        ''' Puts the value in D register to the memory'''
        # Using temp registers R5 and R6
        if segment == 'constant':
            pass
        else:
            self.output_file.write('@internal1' + '\n')
            self.output_file.write('M=D' + '\n')
            self.calculate_address(segment, index)
            self.output_file.write('@internal2' + '\n')
            self.output_file.write('M=D' + '\n')
            self.output_file.write('@internal1' + '\n')
            self.output_file.write('D=M' + '\n')
            self.output_file.write('@internal2' + '\n')
            self.output_file.write('A=M' + '\n')
            self.output_file.write('M=D' + '\n')

    def calculate_address(self, segment, index):
        ''' Calculates the effective address using segment and index and puts in D'''
        if segment == 'local':
            self.output_file.write('@LCL' + '\n')
            self.output_file.write('D=M' + '\n')
            self.output_file.write('@' + str(index) + '\n')
            self.output_file.write('D=D+A' + '\n')
        elif segment == 'argument':
            self.output_file.write('@ARG' + '\n')
            self.output_file.write('D=M' + '\n')
            self.output_file.write('@' + str(index) + '\n')
            self.output_file.write('D=D+A' + '\n')
        elif segment ==  'this':
            self.output_file.write('@THIS' + '\n')
            self.output_file.write('D=M' + '\n')
            self.output_file.write('@' + str(index) + '\n')
            self.output_file.write('D=D+A' + '\n')
        elif segment == 'that':
            self.output_file.write('@THAT' + '\n')
            self.output_file.write('D=M' + '\n')
            self.output_file.write('@' + str(index) + '\n')
            self.output_file.write('D=D+A' + '\n')
        elif segment == 'pointer':
            self.output_file.write('@3' + '\n')
            self.output_file.write('D=A' + '\n')
            self.output_file.write('@' + str(index) + '\n')
            self.output_file.write('D=D+A' + '\n')
        elif segment == 'temp':
            self.output_file.write('@5' + '\n')
            self.output_file.write('D=A' + '\n')
            self.output_file.write('@' + str(index) + '\n')
            self.output_file.write('D=D+A' + '\n')
        elif segment == 'static':
            self.output_file.write('@' + self.input_file + '.' + str(index) + '\n')
            self.output_file.write('D=A' + '\n')


