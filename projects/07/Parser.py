#/usr/bin/python

import re

class Parser:
    def __init__(self, filename):
        self.arithmetic = ['add', 'sub', 'neg', 'eq', 'lt', 'gt', 'and', 'or', 'not']
        self.input_file  = open(filename, 'r')
        self.next_command = self.input_file.readline()


    def has_more_commands(self):
        return True if self.next_command != '' else False

    def advance(self):
        self.current_command = self.next_command
        self.next_command = self.input_file.readline()

        self.current_command = re.sub('\s{2,}', ' ', self.current_command)
        self.current_command = self.current_command.strip()
        if self.current_command.find('//') >= 0:
            self.current_command = self.current_command[0:self.current_command.find('//')]
        self.current_command = self.current_command.strip()
        if self.current_command == '':
            self.advance()

    def command_type(self):
        if self.current_command in self.arithmetic:
            return 'C_ARITHMETIC'
        elif self.current_command.find(' ') is not -1:
            first_token = self.current_command.split(' ')[0]
            if first_token.find('-') is not -1:
                return 'C_' + first_token[:first_token.find('-')]
            else:
                return 'C_' + first_token.upper()

    def arg1(self):
        if self.command_type() == 'C_ARITHMETIC':
            return self.current_command.upper()
        else:
            return self.current_command.split(' ')[1]

    def arg2(self):
        return self.current_command.split(' ')[2]

