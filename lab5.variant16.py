# PI-201 Mamontov Bogdan Serhiyovych V.16
# https://finance.yahoo.com/quote/BNB-USD/history?period1=1510185600&period2=1695081600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('TRX-USD.csv')

volume_class = []
volume_mean = df.Volume.mean()

for volume in df['Volume']:
    if volume + volume * 0.2 > volume_mean > volume - volume * 0.2:
        volume_class.append('Avg_V')
    elif volume - volume * 0.2 < volume_mean:
        volume_class.append('Low_V')
    else:
        volume_class.append('High_V')

df['volume_class'] = volume_class

fig = plt.figure(figsize=(12, 6))
vol = fig.add_subplot(121)
open = fig.add_subplot(122)
vol.hist(df.Volume, bins=80)
vol.set_xlabel('Volume')
vol.set_title("Histogram of Volume")
open.hist(df.Open, bins=80)
open.set_xlabel('Open')
open.set_title("Histogram of Open")
plt.show()

sns.displot(
    data=df,
    x="Open", hue="volume_class",
    kind="kde", height=6,
    multiple="fill", clip=(0, None),
    palette="ch:rot=-.25,hue=1,light=.75",
)
plt.show()

sns.violinplot(x='Open', y='volume_class', data=df)
plt.show()

