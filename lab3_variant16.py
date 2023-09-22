# PI-201 Mamontov Bogdan Serhiyovych V.16
# https://finance.yahoo.com/quote/BNB-USD/history?period1=1510185600&period2=1695081600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

import csv
import datetime
from random import randint

path_file = "TRX-USD.csv"

accuracy = 6

size = 0

date_arr = []
close_arr = []
volume_arr = []

def average(obj):
    return sum(obj) / len(obj)

with open(path_file) as file:
    reader = csv.reader(file)
    next(reader)

    for date, open_t, high, low, close_t, adj, volume in reader:
        date_arr.append(datetime.datetime.strptime(date, "%Y-%m-%d").date())
        close_arr.append(float(close_t) if close_t != 'null' else 0.0)
        volume_arr.append(float(volume) if volume != 'null' else 0)
        size += 1

average_arr = []
for close_item, volume_item in zip(close_arr, volume_arr):
    average_arr.append((close_item + volume_item) / 2)

for num in range(3):
    random_x = randint(0, size)

    print(f"{random_x}) {average_arr[random_x]:.{accuracy}f} ---> "
          f"C:{close_arr[random_x]:{accuracy}f} - V:{volume_arr[random_x]:.{accuracy}f}")

print(f"Close avg: {average(close_arr):.{accuracy}}")
print(f"Volume avg: {average(volume_arr):.{accuracy}}")

