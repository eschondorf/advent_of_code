import util
import math
import time

def find_largest_val_and_index(num, n):
    max_value = max(num[:n])
    for i, digit in enumerate(num):
        if digit == max_value:
            max_index = i
            break
    return max_value, max_index


def solver(inpt):
    rv1 = 0
    rv2 = 0
    for line in inpt:
        bank = [int(x) for x in line]
        max_index = -1
        max_value = max(bank[:-1])
        for i, digit in enumerate(bank):
            if digit == max_value:
                max_index = i
                break
        second_val = max(bank[max_index+1:])
        #print(line)
        #print(int("{}{}".format(max_value, second_val)))
        rv1 += int("{}{}".format(max_value, second_val))

    for line in inpt:
        bank = [int(x) for x in line]
        digits = len(bank)
        val = []
        n = 12
        j = 0
        while n >0:
            max_value, max_index = find_largest_val_and_index(bank[j:], digits-n+1-j)
            val.append(max_value)
            j += max_index + 1
            n -=1
        rv2 += int("".join(map(str, val)))
        
    return rv1, rv2





if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_3_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_3_test.txt", sep = "\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)

