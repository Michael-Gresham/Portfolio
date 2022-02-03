import os
import pickle

main_dir = os.path.split(os.path.abspath(__file__))[0]
if __name__ == "__main__":
    lines = []
    with open(main_dir + "/input.txt") as f:
        lines = f.readlines()
    greater = ""
    lesser = ""
    print(len(lines[0]))
    for num in range(0, len(lines[0]) - 1):
        one = 0
        zero = 0
        for line in lines:
            print(line)
            if line[num] == "1":
                one += 1
            elif line[num] == "0":
                zero += 1
        if one >= zero:
            greater += "1"
            lesser += "0"

        elif zero > one:
            greater += "0"
            lesser += "1"

    print(greater)
    print(lesser)
    total = int(greater, 2) * int(lesser, 2)
    print("Total Energy Consumption: " + str(total))
