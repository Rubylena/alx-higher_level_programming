#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1

    if count == 0:
        print('0 arguments.')
    elif count == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(count))

    for i in range(count):
        # adding 1 to both the range and the argument makes
        # sure that printing starts from 1 and the 2nd argument
        print('{}: {}'.format((i + 1), sys.argv[i + 1]))
