from pathlib import Path
import math

def next_magic_number(number):
    numberAsString = str(number)
    lenght = len(numberAsString)

    if(numberAsString == str(9) * lenght):
        nextNum = number + 2
        return nextNum
    cuttingPoint = math.ceil(lenght / 2)
    part1Str = numberAsString[:cuttingPoint]
    
    def mirrored(part):
        if lenght % 2 == 0:
            return part[::-1]
        else:
            return part[:-1][::-1]
    
    nextNum = part1Str + mirrored(part1Str)
    if int(nextNum) <= number:
        newPart1 = str(int(part1Str) + 1)
        nextNum = newPart1 + mirrored(newPart1)

    return nextNum

def main():
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    
    for line in data: 
        stripped = line.strip()
        if stripped: 
            if "^" in stripped:
                base, index = stripped.split("^")
                number = pow(int(base), int(index))
            else:
                number = int(stripped)
            
            print(next_magic_number(number))



if __name__ == "__main__":
    main()
