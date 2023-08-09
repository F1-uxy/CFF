import sys
import re

lines = []
tokens = []
labels = {}



if len(sys.argv) != 2:
    print("input asm.py 'path_to_file'")
    sys.exit(1)
else:
    file = open(sys.argv[1], 'r')

while True:
    line = file.readline()
    if not line: break
    if line.strip:
        lines.append(line.strip())

file.close()

def clearbin(fn):
    with open("rom.bin", "wb") as file:
        file.close()

def writebin(fn, b):
    with open("rom.bin", "ab") as file:
        file.write(bytearray(b))


clearbin("rom.bin")


# Remove comments and empty space
for i in range(len(lines)):
    lines[i].replace('\n', '')
    lines[i].replace('\r', '')

    if lines[i].find(';') != -1:
        lines[i] = lines[i][0:lines[i].find(';')]

    lines[i] = lines[i].strip()


# Remove empty lines
lines = [i for i in lines if i]


for line in lines:
    token = re.split(r'[, ]',line)
    tokens.append(token)

# Remove empty instructions in the tokens
for i, sublist in enumerate(tokens):
    tokens[i] = [item for item in sublist if item]

for i, line in enumerate(lines):
    if line[0].find('.') != -1:
        labels[line[1:]] = (i*4)
        print("Label: " + line[1:] + "@" + format(i*4, '#04x'))
    


for token in tokens:

    # Check if token is label definition
    if token[0][1:] in labels:
        continue


    if token[0].upper().find('LD') != -1:

        r = int(token[1].upper()[1:])

        if (r >= 0 and r <= 7):
            if token[2].find('@') != -1:
                addr = int(token[2][1:], 16)
                o = [0x02, r, addr]
                writebin("rom.bin", o)
                continue
            elif token[2].find('R') != -1:
                r2 = int(token[2][1:])
                o = [0x01, r, 0, r2]
                writebin("rom.bin", o)
                continue
            elif token[2].find('#') != -1:
                val = int(token[2][1:], 16)
                o = [0x00, r, val >> 8, val & 0xFF]
                writebin("rom.bin", o)
                continue
            else:
                print("Unkown memory/register address")
        else:
            print("Register out of range")

    elif token[0].upper().find('STR') != -1:

        r = int(token[1][1:])
        
        if (r >= 0 and r <= 7):
            if token[2].find('@') != -1:
                if token[0].upper().find('STRL') != -1:
                    addr = int(token[2][1:], 16)
                    o = [0x11, r, addr]

                elif token[0].upper().find('STRH') != -1 :
                    addr = int(token[2][1: ], 16)
                    o = [0x12, r, addr]
                    
                else:    
                    addr = int(token[2][1:], 16)
                    o = [0x10, r, addr]

                writebin("rom.bin", o)
                continue
            elif token[2].find('R') != -1:
                r2 = int(token[2][1:], 16)
                o = [0x13, r, 0, r2]
                writebin("rom.bin", o)
                continue

            else:
                print("Unkown memory/register address")
        else:
            print("Register out of range")

    elif token[0].upper().find('CMP') != -1:

        r = int(token[1][1:])

        if (r >= 0 and r <= 7):
            
            if token[2].find('R') != -1:
                r2 = int(token[2][1:])
                o = (0x20, r, 0,  r2)
                writebin("rom.bin", o)

            elif token[2].find('@') != -1:
                addr = int(token[2][1:], 16)
                o = [0x21, r, addr]
                writebin("rom.bin", o)

            else:
                print ("Unknown memory/register address")
        else:
            print("Register out of range")

    elif token[0].upper() == "BEQ":

        label = token[1]

        if label in labels:
            addr = labels[label]
            o = [0x30, 0, addr]
            writebin("rom.bin", o)
        else:
            print("Label not defined: ", label)
            sys.exit()

    elif token[0].upper() == "BNE":

        label = token[1]

        if label in labels:
            addr = labels[label]
            o = [0x31, 0, addr]
            writebin("rom.bin", o)
        else:
            print("Label not defined: ", label)
            sys.exit()

    elif token[0].upper() == "BGT":

        label = token[1]

        if label in labels:
            addr = labels[label]
            o = [0x32, 0, addr]
            writebin("rom.bin", o)
        else:
            print("Label not defined: ", label)
            sys.exit()

    elif token[0].upper() == "BLT":

        label = token[1]

        if label in labels:
            addr = labels[label]
            o = [0x33, 0, addr]
            writebin("rom.bin", o)
        else:
            print("Label not defined: ", label)
            sys.exit()

    elif token[0].upper() == "BRN":

        label = token[1]

        if label in labels:
            addr = labels[label]
            o = [0x34, 0, addr]
            writebin("rom.bin", o)
        else:
            print("Label not defined: ", label)
            sys.exit()

    elif token[0].upper().find('ADD') != -1:

        r = int(token[1][1:])

        if (r >= 0 and r <= 7):
            if token[2].find('#') != -1:
                val = int(token[2][1:], 0)
                o = [0x40, 0, val]
                writebin("rom.bin", o)
                continue
            elif token[2].find('R') != -1:
                r2 = int(token[2][1:])
                o = [0x42, r, 0, r2]
                writebin("rom.bin", o)
            else:
                print("Unknown memory/register", token)
        else:
            ("Register out of range")

    elif token[0].upper().find('SUB') != -1:

        r = int(token[1][1:])

        if (r >= 0 and r <= 7):
            if token[2].find('#') != -1:
                val = int(token[2][1:], 0)
                o = [0x41, 0, val]
                writebin("rom.bin", o)
                continue
            elif token[2].find('R') != -1:
                r2 = int(token[2][1:])
                o = [0x43, r, 0, r2]
                writebin("rom.bin", o)
            else:
                print("Unknown memory/register", token)
        else:
            ("Register out of range")
    
    elif token[0].upper().find('HALT') != -1:
        o = [0xEE, 0xFF, 0xEE, 0xFF]
        writebin("rom.bin", o)
    
    elif token[0].upper().find('NOOP') != -1:
        o = [0xFF, 0xFF, 0xFF, 0xFF]
        writebin("rom.bin", o)

    else:
        print("Unknown operand: ", token[0])
        
            
        
        


                
                
