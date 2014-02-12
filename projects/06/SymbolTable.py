#!/usr/bin/python

class SymbolTable:
    def __init__(self):
        self.table = {}
        self.add_entry('SP', 0)
        self.add_entry('LCL', 1)
        self.add_entry('ARG', 2)
        self.add_entry('THIS', 3)
        self.add_entry('THAT', 4)
        self.add_entry('R0', 0)
        self.add_entry('R1', 1)
        self.add_entry('R2', 2)
        self.add_entry('R3', 3)
        self.add_entry('R4', 4)
        self.add_entry('R5', 5)
        self.add_entry('R6', 6)
        self.add_entry('R7', 7)
        self.add_entry('R8', 8)
        self.add_entry('R9', 9)
        self.add_entry('R10', 10)
        self.add_entry('R11', 11)
        self.add_entry('R12', 12)
        self.add_entry('R13', 13)
        self.add_entry('R14', 14)
        self.add_entry('R15', 15)
        self.add_entry('SCREEN', 0x4000)
        self.add_entry('KBD', 0x6000)

    def add_entry(self, symbol, address):
        self.table[symbol] = address

    def contains(self, symbol):
        return symbol in self.table

    def get_address(self, symbol):
        return self.table[symbol]
