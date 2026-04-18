from pathlib import Path
from datetime import datetime

def calc_parking_fee(entryTime, exitTime):
    if entryTime > exitTime:
        return "Error: invalid time"
    
    
    duration = exitTime - entryTime
    totalMins = duration.total_seconds() / 60

    if totalMins >= 1440:
        return 10000 #ha 24 oranal tobbet marad akkor ráhívjuk a rendőrséget :D

    if totalMins <= 30:
        return 0
    
    billableMins = totalMins - 30
    fee = 0

    Under3HoursAMin = 300 / 60
    After3HoursAMin = 500 / 60
    if billableMins <= 180:
        fee = billableMins * Under3HoursAMin
    else:
        fee = 180 * Under3HoursAMin
        remainingMins = billableMins - 180
        fee += remainingMins * After3HoursAMin
    
    return round(fee)
        


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    lines = data.splitlines()
    result = []

    for line in lines[2:]:
        parts = line.split()

        plate = parts[0]
        entryStr = f"{parts[1]} {parts[2]}"
        exitStr = f"{parts[3]} {parts[4]}"

        format = "%Y-%m-%d %H:%M:%S"
        entryDate = datetime.strptime(entryStr, format)
        exitDate = datetime.strptime(exitStr, format)

        fee = calc_parking_fee(entryDate, exitDate)
        resultText = f"{plate}: {fee}Ft"
        print(resultText)
        result.append(resultText)


if __name__ == "__main__":
    main()
