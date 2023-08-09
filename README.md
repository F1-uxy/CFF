# CFF

- 16 bit mode = 32 Bit Instructions
- 8 bit mode = 24 Bit Instructions
- 8 bit mode ignores DATA/ADDR H
- Instruction - OPCODE - Data 1 - Data 2 
- Cannot act directly on memory 
- Values must be prefixed with a # 
- Registers must be prefixed with @ 
- Comments are denoted with ; 

| Instuction         | OPCODE | Register | Data/ADDR H | Data/ADDR L |
| ------------------ | ------ | -------- | ----------- | ----------- |
| LD, R1, #0xabcd     | 0x00   | REG[0-7] | 0xAB        | 0xCD        |
| LD R1, R2        | 0x01   | REG[0-7] | 0x00        | REG[0-7]    |
| LD R1, @0xABCD   | 0x02   | REG[0-7] | 0xAB        | 0xCD        |
|                    |        |          |             |             |
| STR R1, @0xABCD  | 0x10   | REG[0-7] | 0xAB        | 0xCD        |
| STRL R1, @0xABCD | 0x11   | REG[0-7] | 0xAB        | 0xCD        |
| STRH R1, @0xABCD | 0x12   | REG[0-7] | 0xAB        | 0xCD        |
| STR R1, R2       | 0x13   | REG[0-7] | 0x00        | REG[0-7]    |
|                    |        |          |             |             |
| CMP R1, R2         | 0x20   | REG[0-7] | 0x00        | REG[0-7]    |
| CMP R1, #0xABCD     | 0x21   | REG[0-7] | 0xAB        | 0xCD        |
|                    |        |          |             |             |
| BEQ LABEL          | 0x30   | 0x00     | 0xAB        | 0xCD        |
| BNE LABEL          | 0x31   | 0x00     | 0xAB        | 0xCD        |
| BGT LABEL          | 0x32   | 0x00     | 0xAB        | 0xCD        |
| BLT LABEL          | 0x33   | 0x00     | 0xAB        | 0xCD        |
| BRN LABEL          | 0x34   | 0x00     | 0xAB        | 0xCD        |
|                    |        |          |             |             |
| ADD R1, #0xABCD     | 0x40   | REG[0-7] | 0xAB        | 0xCD        |
| SUB R1, #0xABCD     | 0x41   | REG[0-7] | 0xAB        | 0xCD        |
| ADD R1, R2         | 0x42   | REG[0-7] | 0x00        | REG[0-7]    |
| SUB R1, R2         | 0x43   | REG[0-7] | 0x00        | REG[0-7]    |
|                    |        |          |             |             |
| HALT               | 0xEE   | 0xFF     | 0xEE        | 0xFF        |
| NOOP               | 0xFF   | 0xFF     | 0xFF        | 0xFF        |
