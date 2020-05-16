import Disassembler
import Simulator


mydis = Disassembler.Disassembler()
output = {}
output = mydis.run()
mydis.print()

mysim = Simulator.Simulator(**output)
mysim.run()
