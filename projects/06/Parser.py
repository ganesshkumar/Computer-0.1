#!/usr/bin/python

class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')
        self.next_command = self.file.readline()

    def has_more_commands(self):
        return True if self.next_command != '' else False

    def get_current_command(self):
        return self.current_command

    def advance(self):
        self.current_command = self.next_command
        self.next_command = self.file.readline()

        self.current_command = self.current_command.replace(' ', '')
        self.current_command = self.current_command.strip()
        if self.current_command.find('//') >= 0:
            self.current_command = self.current_command[0:self.current_command.find('//')]
	if self.current_command[:2] == '//' or self.current_command == '':
            self.advance()

    def command_type(self):
        return 'A_COMMAND' if self.current_command[0] is '@' else 'L_COMMAND' if self.current_command[0] is '(' else 'C_COMMAND'

    def symbol(self):
        return self.current_command[1:] if self.current_command[0] is '@' else self.current_command[1:len(self.current_command)-1]

    def dest(self):
        return self.current_command[0:self.current_command.find('=')] if self.current_command.find('=') >= 1 else 'null'

    def comp(self):
        return self.current_command[self.current_command.find('=')+1:] if self.current_command.find('=') >= 1 else self.current_command[:self.current_command.find(';')] if self.current_command.find(';') >= 1 else self.current_command

    def jump(self):
        if self.current_command.find('JGT') >= 0:
            return 'JGT'
        elif self.current_command.find('JEQ') >= 0:
            return 'JEQ'
        elif self.current_command.find('JGE') >= 0:
            return 'JGE'
        elif self.current_command.find('JLT') >= 0:
            return 'JLT'
        elif self.current_command.find('JNE') >= 0:
            return 'JNE'
        elif self.current_command.find('JLE') >= 0:
            return 'JLE'
        elif self.current_command.find('JMP') >= 0:
            return 'JMP'
        else :
           return 'null'
