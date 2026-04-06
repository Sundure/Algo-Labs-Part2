import os
from enum import Enum

class DetectorVerdict(Enum):
    SAFE = 0,
    UNSAFE = 1

class SmokeDetector():
    def __init__(self, smoke_value: float) -> None:
        self.smoke_value: float = smoke_value

    def get_verdict(self) -> DetectorVerdict:
        if self.smoke_value >= 1:
            return DetectorVerdict.UNSAFE
        else:
            return DetectorVerdict.SAFE

def zig_zag_smoke_detector_check(detectors: list[list[SmokeDetector]]) -> DetectorVerdict:
    current_cycle = 0
    current_column = 0
    current_step = 0
    reverse = True
    
    while True:
        if current_cycle == len(detectors) * len(detectors[0] ):
            return DetectorVerdict.SAFE

        if reverse:
            current_column = min(current_cycle, len(detectors) - 1)
        else:
            current_column = max(0, current_cycle - len(detectors[0]) + 1)

        while current_column in range(len(detectors)):
            if current_column > current_cycle or current_cycle - current_column >= len(detectors[0]):
                break
            if detectors[current_column][current_cycle - current_column].get_verdict() == DetectorVerdict.UNSAFE:
                print(f"Coordinate: [{current_column}, {current_cycle - current_column}]")
                print(f"Step: {current_step +1}")
                return DetectorVerdict.UNSAFE
            if reverse:
                current_column -= 1
            else:
                current_column += 1
            current_step += 1

        reverse = not reverse
        current_cycle += 1

class Program():
    @staticmethod
    def main() -> None:
        while True:
            print("Fire Report Anilizer")
            print()

            print("Press: Y To Show Current Report")
            print("Press: E To Close Program")

            print()

            pressed_key = input("Press: One Of This Key To Chose Action: ")

            print(pressed_key)
            if pressed_key in ("y","Y"):
                os.system("clear")
                detectors = [[SmokeDetector(0),SmokeDetector(0),SmokeDetector(0)], [SmokeDetector(0),SmokeDetector(0),SmokeDetector(1)]]
                print(f"START REPORT: \n")

                print(zig_zag_smoke_detector_check(detectors))
                print()
                print("END REPORT: ")
                print()
            elif pressed_key in ("e","E"):
                exit()
            else:
                print(f"Invalid Input: Try Again \n")


Program.main()
