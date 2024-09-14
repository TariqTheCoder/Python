import csv
import random
rows = []

with open("in.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        rows.append(row)

raw_input = input("Type a word -> ")
with open ("out.csv", "w", newline="\n") as f:
    writer = csv.writer(f)
    writer.writerow([raw_input])
print("Done")