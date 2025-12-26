import util
import math
import time

def solver(inpt):
    rv1 = 0
    rv2 = 0
    cur = 50
    for line in inpt:
        #print(line)
        direction = line[0]
        val = int(line[1:])
        reduced_val = val%100
        if direction == 'L':
            reduced_val = -1*reduced_val
            if cur != 0 and -1*reduced_val > cur:
                rv2 += 1
          #      print("hit going left")
        if direction == 'R':
            if cur != 0 and reduced_val + cur > 100:
                rv2+= 1
         #       print("hit going right")
        rv2 += max(0, abs(val)//100)
        #print("additional go arounds are: ", max(0, abs(val)//1000))
        cur = (cur + reduced_val)%100
        if cur == 0:
            rv1 +=1
            rv2 += 1
            #print("BINGO!")
        #print(rv2)
        #print(cur)
    
    return rv1, rv2





if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_1_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_1_test.txt", sep = "\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)

