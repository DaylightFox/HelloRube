class VM:
    
    def __init__(self):
        self.mem = [0 for i in range(0, 65536)]
        self.i = 65535 # stack pointer

    def __InterpretInstruction(self, cmd:str):
        # cmd is only one char
        if cmd == 'n':
            self.i -= 1
        elif cmd == 'b':
            self.i += 1
        elif cmd == 'p':
            print(chr(self.mem[self.i]), end='')
        elif cmd == '+':
            self.mem[self.i+1] = self.mem[self.i] + self.mem[self.i+1]
        elif cmd == '-':
            self.mem[self.i+1] = self.mem[self.i] - self.mem[self.i+1]
        elif cmd == '*':
            self.mem[self.i+1] = self.mem[self.i] * self.mem[self.i+1]
        elif cmd == '/':
            self.mem[self.i+1] = self.mem[self.i] / self.mem[self.i+1]
        elif cmd == 'g':
            self.mem[self.i] = self.mem[self.mem[self.i]]
        elif cmd == 's':
            self.mem[self.mem[self.i]] = self.mem[self.i+1]
        else:
            self.mem[self.i] = ord(cmd) - ord('0') 

    def ExecuteInstructions(self, instructions:str):
        for ch in instructions:
            self.__InterpretInstruction(ch)


if __name__ == "__main__":
    myVM = VM()
    myVM.ExecuteInstructions('xpdna+bpn7+bppn3+bpPpnf+1+bpnH+bpn3+bpn)n1+b+bpn++4+bpQp')
    print()