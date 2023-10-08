# PI-201 Mamontov Bogdan Serhiyovych V.16
# https://finance.yahoo.com/quote/BNB-USD/history?period1=1510185600&period2=1695081600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

from numpy import array, average
import csv
import datetime
from random import randint
import time

timer = time.time()

path_file = "TRX-USD.csv"

accuracy = 6

size = 0

date_arr = []
close_arr = []
volume_arr = []

with open(path_file) as file:
    reader = csv.reader(file)
    next(reader)

    for date, open_t, high, low, close_t, adj, volume in reader:
        date_arr.append(datetime.datetime.strptime(date, "%Y-%m-%d").date())
        close_arr.append(float(close_t) if close_t != 'null' else 0.0)
        volume_arr.append(float(volume) if volume != 'null' else 0.0)
        size += 1

arrayTime = time.time()

close_arr = array(close_arr)
volume_arr = array(volume_arr)

average_arr = (close_arr+volume_arr)/2

print(f"Array parse time: {time.time() - arrayTime}")

for num in range(3):
    random_x = randint(0, size)

    print(f"{random_x}) {average_arr[random_x]:.{accuracy}f} ---> "
          f"С:{close_arr[random_x]:{accuracy}f} - V:{volume_arr[random_x]:.{accuracy}f}")

print(f"Close avg: {average(close_arr):.{accuracy}}")
print(f"Volume avg: {average(volume_arr):.{accuracy}}")


print(f"Time working: {time.time() - timer}")