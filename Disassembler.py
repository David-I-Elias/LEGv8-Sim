# This File serves as the main translator for the project. 
# Raw binary instructions are read in from the input file and
# translated to ARM instructions here. Once all instructions
# have been translated they are returned as a Dict

from Helper import SetUp
import os
import Masking_Constants as MASKs
import sys


class Disassembler:

    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    dataval = []
    rawdata = []
    address = []
    numInstructs = 0
    breakVal = 0

    def __init__(self):
        self.Masking_Constants = MASKs
        self.bMask = MASKs.bMask
        self.jAddrMask = MASKs.jAddrMask
        self.specialMask = MASKs.specialMask
        self.rnMask = MASKs.rnMask
        self.rmMask = MASKs.rmMask
        self.rdMask = MASKs.rdMask
        self.imMask = MASKs.imMask
        self.shmtMask = MASKs.shmtMask
        self.addrMask = MASKs.addrMask
        self.addr2Mask = MASKs.addr2Mask
        self.imsftMask = MASKs.imshftMask
        self.imdataMask = MASKs.imdataMask

    def run(self):

        instructions = []
        instructions = SetUp.import_data_file()

        outputFilename = SetUp.get_output_filename()

        print("raw output filename is ", outputFilename)

        for i in range (len(instructions)):
            self.address.append((96 + (i * 4)))

        opcode = []

        for z in instructions:
            opcode.append(int(z, base=2) >> 21)


        #opcode searching starts here
        for i in range(len(opcode)):
            self.numInstructs = self.numInstructs + 1
            if opcode[i] == 1112:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ADD")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))


            elif opcode[i] == 1624:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("SUB")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))

            elif opcode[i] == 1104:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("AND")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))

            elif opcode[i] == 1360:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ORR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))

            elif opcode[i] == 1690:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(" #" + str(self.arg2[i]))


            elif opcode[i] == 1691:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSL")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(" #" + str(self.arg2[i]))


            elif opcode[i] == 1692:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ASR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(" #" + str(self.arg2[i]))


            elif opcode[i] == 1872:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("EOR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))

            elif opcode[i] == 1160 or opcode[i] == 1161:
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("ADDI")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.imMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))

            elif opcode[i] == 1672 or opcode[i] == 1673:
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("SUBI")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.imMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))

            # D type
            elif opcode[i] == 1984:
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("STUR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.addrMask) >> 12)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", [R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]) + "]")

            elif opcode[i] == 1986:
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("LDUR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.addrMask) >> 12)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", [R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]) + "]")

            # B type
            elif (opcode[i] >= 160 and opcode[i] <= 191):
                self.instrSpaced.append(SetUp.bin2StringSpacedB(instructions[i]))
                self.opcodeStr.append("B")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & self.bMask), 26))
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("\t#" + str(self.arg1[i]))
                self.arg2Str.append("")
                self.arg3Str.append("")

            # CB type
            elif (opcode[i] >= 1440 and opcode[i] <= 1447):
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBZ")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2)& self.addr2Mask) >> 5, 19)) 
                self.arg2.append((int(instructions[i], base=2) & self.rdMask) >> 0) 
                self.arg3.append(0)
                self.arg1Str.append("\tR" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")

            elif (opcode[i] >= 1448 and opcode[i] <= 1455):
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBNZ")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2)& self.addr2Mask) >> 5, 19)) 
                self.arg2.append((int(instructions[i], base=2) & self.rdMask) >> 0) 
                self.arg3.append(0)
                self.arg1Str.append("\tR" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")


            # IM type - missing imdataMask, field unsigned value
            elif (opcode[i] >= 1684 and opcode[i] <= 1687):
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("MOVZ")
                self.arg1.append(SetUp.movShift((int(instructions[i], base=2) & self.imsftMask) >> 21))
                self.arg2.append((int(instructions[i], base=2) & self.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg1[i]))


            elif (opcode[i] >= 1940 and opcode[i] <= 1943):
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("MOVZK")
                self.arg1.append(SetUp.movShift((int(instructions[i], base=2) & self.imsftMask) >> 21))
                self.arg2.append((int(instructions[i], base=2) & self.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg1[i]))

            #NO-OP

            elif(opcode[i] == 0):
                self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("NOP")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")


            #BREAK INST.

            elif opcode[i] == 2038 and (int(instructions[i], base=2) & self.specialMask) == 2031591:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("BREAK")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.breakVal = i
                print("breaking")
                break

            #NOT FOUND

            else:
                self.opcodeStr.append("unknown")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                print("i =:  " + str(i))
                print("opcode =:  " + str(opcode[i]))
                sys.exit("Instruction not found.")


        for i in range(len(opcode)):
            j = 0
            if opcode[i] == 2038 and (int(instructions[i], base=2) & self.specialMask) == 2031591:
                 self.address[i] + (i *4)
                 while i+1 in range(len(instructions)):
                     self.rawdata.append(instructions[i+1])
                     self.dataval.append(SetUp.imm_32_bit_unsigned_to_32_bit_signed_converter(int(self.rawdata[j], base=2)))
                     j += 1
                     i += 1

        return {"instructions": instructions,
                "opcode": opcode,
                "opcodeStr": self.opcodeStr,
                "arg1": self.arg1,
                "arg1Str": self.arg1Str,
                "arg2": self.arg2,
                "arg2Str": self.arg2Str,
                "arg3": self.arg3,
                "arg3Str": self.arg3Str,
                "dataval": self.dataval,
                "address": self.address,
                "numInstructs": self.numInstructs}


    def print(self):
        outFile = open(SetUp.get_output_filename() + "dis.txt", 'w')

        for i in range(self.numInstructs):
            outFile.write(str(self.instrSpaced[i]) + '\t' + str(self.address[i]) + '\t' + str(self.opcodeStr[i]) + '\t' + str(self.arg1Str[i]) + str(self.arg2Str[i]) + str(self.arg3Str[i]) + "\n")

        for i in range(len(self.dataval)):
            outFile.write(str(self.rawdata[i]) + '\t' + str(self.address[self.breakVal + (i+1)]) + '\t' + str(self.dataval[i]) + "\n")

        outFile.close()
