#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # count = len(sys.argv) - 1

    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
        # this print gives the addition of the arguments one by one
        # print('{}'.format(sum))
    # this print gives the total sum of argument
    print('{}'.format(sum))
