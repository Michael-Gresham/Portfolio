import pickle
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

if __name__ == "__main__":
    lines = []
    with open(main_dir + "/input.txt") as f:
        lines = f.readlines()

    count = 0
    current = int(lines.pop(0))
    for x in lines:
        if int(x) >= current:
            count = count + 1
        current = int(x)
    print()
    print(count)
    f.close()
