import util
import math
import time


def solver(inpt):
    rv1 = 0
    rv2 = 0
    for line in inpt:
        start, end = [int(x) for x in line.split("-")]
        for num in range(start, end + 1):
            #print()
            #print(num)
            len_split = int(math.log(num, 10) + 1)
            digits = len(str(num))
            largest_len_split = int(digits/2)
            while largest_len_split >=1:
                #print(largest_len_split)
                i = digits // largest_len_split
                repeating = True
                if int(digits/largest_len_split) == digits/largest_len_split:
                    repeating_part = int(str(num)[:int(largest_len_split)])
                    for j in range(1, i):
                        #print(22, j, largest_len_split)
                        #print(type(largest_len_split*(j+1)))
                        #print(str(num)[largest_len_split*(j): largest_len_split*(j+1)])
                        if repeating_part != int(str(num)[largest_len_split*(j): largest_len_split*(j+1)]):
                            #print("I'm not repeating")
                            repeating = False
                    if repeating:
                       # print("I'm repeating!")
                        rv2 += num
                        break

                largest_len_split -= 1
                i += 1
            #print(len_split)
            if len_split %2 == 0:
                #print(int(str(num)[0:len_split//2]), int(str(num)[len_split//2:]))
                if int(str(num)[0:len_split//2]) == int(str(num)[len_split//2:]):
                    rv1 += num
                    #print("symmetric number!")

    return rv1, rv2





if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_2_input.txt", sep = ",")
    tst = util.read_strs("inputs/day_2_test.txt", sep = ",")
    tst1 = ["11-22", "95-115", "998-1012", "1188511880-1188511890"]

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)

