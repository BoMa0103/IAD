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
high = fig.add_subplot(122)
vol.hist(df.Volume, bins=80)
vol.set_xlabel('Volume')
vol.set_title("Histogram of Volume")
high.hist(df.High, bins=80)
high.set_xlabel('High')
high.set_title("Histogram of High")
plt.show()

sns.jointplot(x="High", y="Volume", data=df, kind='reg', fit_reg=True)
plt.show()

sns.stripplot(data=df, x="High", y="volume_class", hue="volume_class", legend=False)
plt.show()

sns.displot(
    data=df,
    x="High", hue="volume_class",
    kind="kde", height=6,
    multiple="fill", clip=(0, None),
    palette="ch:rot=-.25,hue=1,light=.75",
)
plt.show()

sns.pairplot(df, hue="volume_class")
plt.show()

sns.violinplot(x='High', y='volume_class', data=df)
plt.show()

sns.pointplot(data=df, x="High", y="volume_class")
plt.show()

clarity_ranking = ["Avg_V", "High_V", "Low_V"]
sns.boxenplot(x="High", y="volume_class",
              color="b", order=clarity_ranking,
              scale="linear", data=df)
plt.show()
