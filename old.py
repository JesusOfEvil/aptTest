#! /usr/bin/ python3

import sys
print("Enter numbers")
out_of = int(sys.argv[1])
while 1:
    line = input()
    total = 0
    for num in line.split(" "):
        total += int(num)
    print("Total: %d (%f%%)" % (total, total * (100.0 / out_of)))
    print('Elliots first chnage')
	print("Enter numbers")
