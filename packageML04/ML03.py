# 1. Loading the csv using standard library

import csv

filename = open("indians-diabetes.data.csv", "r")
reader = csv.reader(filename, delimiter=",")        #reader() function by default reads the entire line
lines = list(reader)        #its an array of 768 instances

print("\n\nNo. of Rows:- ", len(lines), "\n\n")

print(lines)

for l in lines:
    print("\n\n", l)

filename.close()
