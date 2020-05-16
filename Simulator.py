from State import State
from Helper import SetUp
import Masking_Constants as MASKs


class Simulator:

    def __init__(self, instructions, opcode, dataval, address, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str,
                 arg2Str, arg3Str):

        self.instructions = instructions
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.specialMask = MASKs.specialMask


        self.outputFileName = SetUp.get_output_filename()

    def run(self):
        foundBreak = False
        armState = State(self.instructions, self.opcode, self.dataval, self.address, self.arg1, self.arg2, self.arg3,
                         self.numInstructs, self.opcodeStr, self.arg1Str, self.arg2Str, self.arg3Str)

        # "Beginning and end of simulator"
        while (foundBreak == False):

            jumpAddr = armState.PC
            i = armState.getIndexOfMemAddress(armState.PC)

            if (self.opcode[i] == 1160 or self.opcode[i] == 1161):  # addi arg3 = rd, arg2 = im, arg1 = rn
                State.R[self.arg3[i]] = State.R[self.arg1[i]] + self.arg2[i]

            elif (self.opcode[i] == 1872):  # eor R3 = R2 ^ R1
                State.R[self.arg3[i]] = State.R[self.arg1[i]] ^ State.R[self.arg2[i]]

            elif (self.opcode[i] == 1692):  # asr R3 = R1 >> Shamt
                State.R[self.arg3[i]] = State.R[self.arg1[i]] >> self.arg2[i]

            elif (self.opcode[i] == 1691):  # lsl R3 = R1 << Shamt
                State.R[self.arg3[i]] = State.R[self.arg1[i]] << self.arg2[i]

            elif (self.opcode[i] == 1690):  # lsr R3 = R1 shifted Shamt right, padded w/ zeros
                State.R[self.arg3[i]] = ((State.R[self.arg1[i]] % 0x100000000) >> self.arg2[i])

            elif (self.opcode[i] == 1360):  # orr R3 = R2 | R1
                State.R[self.arg3[i]] = State.R[self.arg1[i]] | State.R[self.arg2[i]]

            elif (self.opcode[i] == 1104):  # and R3 = R2 & R1
                State.R[self.arg3[i]] = State.R[self.arg1[i]] & State.R[self.arg2[i]]

            elif (self.opcode[i] == 1624):  # sub
                State.R[self.arg3[i]] = State.R[self.arg1[i]] - State.R[self.arg2[i]]

            elif (self.opcode[i] == 1112):  # add
                State.R[self.arg3[i]] = State.R[self.arg1[i]] + State.R[self.arg2[i]]

            elif (self.opcode[i] == 1672 or self.opcode[i] == 1673):  # SUBI
                State.R[self.arg3[i]] = State.R[self.arg1[i]] - self.arg2[i]

            elif (self.opcode[i] == 1984):  # STUR
                try:
                    self.dataval[(armState.getIndexOfMemAddress((self.arg2[i] * 4) + State.R[self.arg1[i]])) - self.numInstructs] = State.R[self.arg3[i]]
                except (IndexError, ValueError):
                    outOfBoundsAddr = (self.arg2[i] * 4) + State.R[self.arg1[i]]
                    if outOfBoundsAddr < 96:
                        print("Address is smaller than 96. Only use addresses greater than 96 when " +
                              "branching/storing/loading.\nFound at instruction number " + str(i+1))
                        sys.exit(0)
                    else:
                        numOfExtraAddr = (outOfBoundsAddr - self.address[len(self.address) -1]) / 4
                        j = 0
                        while j < numOfExtraAddr:
                            self.address.append(self.address[len(self.address) - 1] + 4)
                            self.dataval.append(0)
                            j+=1
                    self.dataval[(armState.getIndexOfMemAddress((self.arg2[i] * 4) + State.R[self.arg1[i]])) - self.numInstructs] = State.R[self.arg3[i]]

            elif (self.opcode[i] == 1986):  # LDUR
                try:
                  State.R[self.arg3[i]] = self.dataval[armState.getIndexOfMemAddress((self.arg2[i] * 4) + State.R[self.arg1[i]]) - self.numInstructs]
                except (IndexError, ValueError):
                    outOfBoundsAddr = (self.arg2[i] * 4) + State.R[self.arg1[i]]
                    if outOfBoundsAddr < 96:
                        print("Address is smaller than 96. Only use addresses greater than 96 when " +
                              "branching/storing/loading.\nFound at instruction number " + str(i+1))
                        sys.exit(0)
                    else:
                        numOfExtraAddr = (outOfBoundsAddr - self.address[len(self.address) - 1]) / 4
                        j = 0
                        while j < numOfExtraAddr:
                            self.address.append(self.address[len(self.address) - 1] + 4)
                            self.dataval.append(0)
                            j+=1
                        State.R[self.arg3[i]] = self.dataval[(armState.getIndexOfMemAddress((self.arg2[i] * 4) + State.R[self.arg1[i]])) - self.numInstructs]

            elif (self.opcode[i] >= 1440 and self.opcode[i] <= 1447):  # CBZ
                if State.R[self.arg2[i]] == 0:
                    jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
                    if jumpAddr < 96:
                        print("Address is smaller than 96. Only use addresses greater than 96 when " +
                              "branching/storing/loading.\nFound at instruction number " + str(i+1))
                        sys.exit(0)
                    if jumpAddr > self.address[self.numInstructs - 1]:
                        print("Address is greater break's address:" + self.address[self.numInstructs - 1] + "."
                              "Only use addresses less than the break's address when branching.\n"
                              "Found at instruction number " + str(i+1))
                        sys.exit(0)

            elif (self.opcode[i] >= 1448 and self.opcode[i] <= 1455):  # CBNZ
                if State.R[self.arg2[i]] != 0:
                    jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
                    if jumpAddr < 96:
                        print("Address is smaller than 96. Only use addresses greater than 96 when " +
                              "branching/storing/loading.\nFound at instruction number " + str(i+1))
                        sys.exit(0)
                    if jumpAddr > self.address[self.numInstructs - 1]:
                        print("Address is greater break's address:" + self.address[self.numInstructs - 1] + "."
                              "Only use addresses less than the break's address when branching.\n"
                              "Found at instruction number " + str(i+1))
                        sys.exit(0)

            elif (self.opcode[i] >= 1684 and self.opcode[i] <= 1687):  # MOVZ
                State.R[self.arg3[i]] = self.arg2[i] << self.arg1[i]

            elif (self.opcode[i] >= 1940 and self.opcode[i] <= 1943):  # MOVZK
                State.R[self.arg3[i]] = (self.arg2[i] << self.arg1[i]) ^ State.R[self.arg3[i]]

            elif (self.opcode[i] == 0):  # NOP
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue

            elif (self.opcode[i] >= 160 and self.opcode[i] <= 191):  # B
                jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
                if jumpAddr < 96:
                    print("Address is smaller than 96. Only use addresses greater than 96 when " +
                          "branching/storing/loading.\nFound at instruction number " + str(i+1))
                    sys.exit(0)
                if jumpAddr > self.address[self.numInstructs - 1]:
                    print("Address is greater break's address:" + self.address[self.numInstructs - 1] + "."
                          "Only use addresses less than the break's address when branching.\n"
                          "Found at instruction number " + str(i+1))
                    sys.exit(0)


            elif self.opcode[i] == 2038:
                foundBreak = True

            else:
                print("-- UNKNOWN INSTRUCTION IN SIM --")

            armState.printState()
            armState.PC = jumpAddr
            armState.incrementPC()
            armState.cycle += 1



