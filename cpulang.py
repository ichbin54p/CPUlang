from sys import argv
import os

class tools:
    def exs(f: str):
        print(f"Creating directory {f}", end="\r")
        if not os.path.exists(f):
            os.mkdir(f)
            print()
        else:
            print(f"Directory {f} already exists")
        return os.path.exists(f)

class main:
    def __init__(self):
        self.argv = argv
        self.command = argv[1]
        if len(self.argv) > 1:
            self.operands = argv[2:]
        else:
            self.operands = []
    def main(self):
        match self.command:
            case "create":
                tools.exs(self.operands[0])
                tools.exs(f"{self.operands[0]}/src")
                tools.exs(f"{self.operands[0]}/config")
                tools.exs(f"{self.operands[0]}/build")
                tools.exs(f"{self.operands[0]}/temp")
                tools.exs(f"{self.operands[0]}/out")
                with open(f"{self.operands[0]}/config/sources.cfg", "w") as f:
                    f.write("CM=COMPILER_PLACEHOLDER\nEX=EXECUTE_PLACEHOLDER")
                with open(f"{self.operands[0]}/config/cpu.cfg", "w") as f:
                    f.write("# CPU SETTINGS\n\nREGISTER_COUNT=8\nPORT_COUNT=8\nRAM_BYTES=64\n# PROGRAM SETTINGS\n\nSIMULATION_SPEED=1")
                with open(f"{self.operands[0]}/src/main", "w") as f:
                    f.write("LDI 8\nRST 2\nPST 0")
            case "build":
                pass

if __name__ == "__main__":
    main().main()