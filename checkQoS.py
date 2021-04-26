import sys


file = open('pjsipchannelstats.log', 'r')
# Lines = file.readlines()

count = 0
for line in file:
    fields = line.strip().split()
    print(fields[0])
    # count += 1
    # print("Line{}: {}".format(count, line.strip()))