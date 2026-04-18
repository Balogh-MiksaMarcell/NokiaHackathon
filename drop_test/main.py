from pathlib import Path

def min_num_of_drops(devices, height):
    if devices == 1:
        return height
    
    reach = [0] * (devices + 1)
    attempts = 0

    while reach[devices] < height:
        attempts += 1

        for i in range(devices, 0, -1):
            reach[i] = reach[i] + reach[i-1] + 1
    
    return attempts

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()
