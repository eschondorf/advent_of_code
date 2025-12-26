import util
import math
import time
import numpy as np


#An attempt at this problem using python's sets. This took too long to run
def create_set(ranges):
    fresh = set()
    for line in ranges:
        start, end = line.split("-")
        for i in range(int(start), int(end) + 1):
            fresh.add(i)

    return fresh


# Takes a list of ranges and condenses it to a new list of "unioned" ranges
def condenser(ranges):
    #print(ranges)
    # Sort ranges by the first number
    ranges = sorted(
    ranges, 
    key=lambda x: x[0]
) 
    #print(ranges)
    condensed_ranges = []
    i = 0
    while i < len(ranges):
        line = ranges[i]
        start, end = line
        #print()
        #print(line)
        #print()
        #print("comparing")
        for j, line2 in enumerate(ranges[i+1:]):
            #print(j)
            #print(line2)
            a, b = line2
            if  end < a: #start of next range is greater than end of current range, break off range and add to condensed list
                condensed_ranges.append([start, end])
                i += j # How far to jump ahead
                #print("end < a")
                break
            elif line2 == ranges[-1]:
                end = max(b, end)
                condensed_ranges.append([start, end])
                i += j
                #print("I'm at the end")
                break
            elif a<=end and end < b: #[1,3] [2,4] -> [1, 4]
                end = b
                #print(" a<=end and end < b")
            elif a <= end and b<=end: #[1,5] [2,3] -> [1, 5]
                #print("a<=end and b<=end")
                continue

        i += 1
    if ranges[-1][0] > condensed_ranges[-1][1]:
        condensed_ranges.append(ranges[-1])
    #print(condensed_ranges)
    return condensed_ranges

    

    
                


def solver(inpt):
    ranges, inventory = inpt[0].split('\n'), inpt[1].split('\n')
    rv1 = 0
    rv2 = 0
    #fresh = create_set(ranges)
    n=1
    max_val = -1
    #print(fresh)
    r = []
    for elt in inventory:
        for line in ranges:
            start, end = line.split("-")
            start, end = int(start), int(end)
            max_val = max(end, max_val)
            if start <= int(elt) <= end:
                rv1 += 1
                break

    for line in ranges:
        start, end = line.split("-")
        start, end = int(start), int(end)
        r.append([start, end])
    
    r_c = condenser(r)
    for a, b in r_c:
        rv2 += b-a + 1


    return rv1, rv2



if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_5_input.txt", sep = "\n\n")
    tst = util.read_strs("inputs/day_5_test.txt", sep = "\n\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)
