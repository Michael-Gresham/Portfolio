import pickle
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

if __name__ == "__main__":
    lines = []
    with open(main_dir + "/input.txt") as f:
        lines = f.readlines()
    out_of_range = False
    count = -1  # Note starts at negative one to take into account the first comparison.
    current = 0
    start = "Start: " + str(current)
    for x in range(0, len(lines)):
        sum = 0
        for y in range(0, 3):
            try:
                sum += int(lines[x + y])
            except:
                out_of_range = True
                break

        if out_of_range == True:
            break

        if sum > current:
            count += 1
        current = sum
    print()
    print(count)
    f.close()
