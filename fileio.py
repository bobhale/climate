import csv

with open('temperaturetest.txt', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

print(int(your_list[5][1]) * 3)

