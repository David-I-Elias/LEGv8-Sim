import sys


class SetUp:

    def __init__(self):
        pass

    @classmethod
    def get_input_filename(cls):
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                inputFileName = sys.argv[i + 1]

        return inputFileName

    @classmethod
    def get_output_filename(cls):
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-o' and i < (len(sys.argv) - 1):
                outputFileName = sys.argv[i + 1]

        return outputFileName

    @classmethod
    def import_data_file(cls):
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                inputFileName = sys.argv[i + 1]
        try:
            instructions = [line.rstrip() for line in open(inputFileName, 'r')]
        except IOError:
            print("Could not find input file, is path correct?")

        return instructions

    @classmethod
    def imm_bit_to_32_bit_converter(cls, num, bitsize):
        if bitsize < 32:
            extendMask = 0xFFFFF000
            extendMask2 = 0xFF000000
            extendMask3 = 0xFFF80000
            extendMask4 = 0xFFFF
            negBitMask = 0x800
            negBitMask2 = 0x2000000
            negBitMask3 = 0x40000
            negBitMask4 = 0x8000

            if bitsize == 12:
                if negBitMask & num > 0:
                    num = num | extendMask
                    num = num ^ 0xFFFFFFFF
                    num = num + 1
                    num = num * -1
            elif bitsize == 26:
                if negBitMask2 & num > 0:
                    num = num | extendMask2
                    num = num ^ 0xFFFFFFFF
                    num = num + 1
                    num = num * -1
            elif bitsize == 19:
                if negBitMask3 & num > 0:
                    num = num | extendMask3
                    num = num ^ 0xFFFFFFFF
                    num = num + 1
                    num = num * -1
            elif bitsize == 16:
                if negBitMask4 & num > 0:
                    num = num | extendMask4
                    num = num ^ 0xFFFFFFFF
                    num = num + 1
                    num = num * -1
            else:
                num = num | 0x0000
        else:
            print("Incorrect Bit Length")

        return num

    @classmethod
    def bin2StringSpaced(cls, s):
        spacedStr = s[0:8] + " " + s[8:11] + " " + s[11:16] + " " + s[16:21] + " " + s[21:26] + " " + s[26:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedR(cls, s):
        spacedStr = s[0:11] + " " + s[11:16] + " " + s[16:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedD(cls, s):
        spacedStr = s[0:11] + " " + s[11:20] + " " + s[20:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedIM(cls, s):
        spacedStr = s[0:9] + " " + s[9:11] + " " + s[11:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedCB(cls, s):
        spacedStr = s[0:8] + " " + s[8:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedI(cls, s):
        spacedStr = s[0:10] + " " + s[10:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedB(cls, s):
        spacedStr = s[0:6] + " " + s[6:32]
        return spacedStr

    @classmethod
    def imm_32_bit_unsigned_to_32_bit_signed_converter(cls, num):
        negBitMask = 0x80000000

        if negBitMask & num > 0:
            num = num ^ 0xFFFFFFFF
            num = num + 1
            num = num * -1
        return num

    @classmethod
    def decimalToBinary(cls, num):
        if num > 1:
            cls.decimalToBinary(num // 2)
        print(num % 2, end="")  # X_X + OwO

    @classmethod
    def binaryToDecimal(cls, binary):
        print("\n")
        decimalNum = (int(binary, 2))
        return decimalNum

    @classmethod
    def movShift(cls, num):
        if num == 0:
            return 0
        elif num == 1:
            return 16
        elif num == 2:
            return 32
        elif num == 3:
            return 48
        else:
            print("error: bit size larger than 2")

    @classmethod
    def getIndexOfMemAddress(cls, currAddr, isSW, dataval, address, numInstructions):
        tempIndex = 0
        try:
            if isSW:
                if len(address) > numInstructions:
                    lastInstructAddr = ((numInstructions - 1) * 4) + 96
                    lastMemAddr = lastInstructAddr +  4 * len(dataval)
                    if currAddr == lastMemAddr:
                        dataval.append(0)
                        dataval.append(0)
                        address.append(lastMemAddr + 4)
                        address.append(lastMemAddr + 8)
                    if currAddr > lastMemAddr:
                        addIndex = (currAddr - lastMemAddr) / 4
                        for i in range(int(addIndex)):
                            dataval.append(0)
                            address.append(lastMemAddr + (4 * (i + 1)))
                tmpIndex = address.index(currAddr)
                tmpIndex = tmpIndex - numInstructions

            else:
                tmpIndex = address.index(currAddr)

                if tmpIndex >= numInstructions:
                    tmpIndex = tmpIndex - numInstructions

            return tmpIndex
        except ValueError:
            print("ERROR -- didn't find memory address currAddr " + str(currAddr))
