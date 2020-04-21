import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dd_aalb_24aar_2019k4 = pd.read_csv(
    'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=851&ALDER=24&Tid=2019K4', delimiter=';')

# print(np.array(dd_aalb_24aar_2019k4))
# Divorced danes in 2008K1 and 2020K1
dd_5a = pd.read_csv(
    'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=F&Tid=2008K1%2C2020K1', delimiter=';')
# print(dd_5a)
# print("Change in pct of divorced danes from 2008K1 to 2020K1 is %5.2f pct" %
#       ((dd_5a['INDHOLD'][1] / dd_5a['INDHOLD'][0] - 1) * 100))


# Which of the 5 biggest cities has the highest percentage of 'Never Married'?
dd_5b = pd.read_csv(
    'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=U', delimiter=';')
# print(dd_5b)
not_cities = ["Hele landet", "Region Hovedstaden", "Region Sjælland",
              "Region Syddanmark", "Region Midtjylland", "Region Nordjylland"]

cities = dd_5b[~dd_5b['OMRÅDE'].isin(not_cities)].sort_values([
    'INDHOLD'], ascending=False)[:5]
# print("5 biggest cities has the highest percentage of 'Never Married'\n", cities)

dd_5c = pd.read_csv(
    'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=*&Tid=*', delimiter=';').sort_values(['TID'])

# print(dd_5c)
# dd_5c.plot.bar()
# plt.show()

# Show a bar chart of 'Married' and 'Never Married' for all ages in DK (Hint: 2 bars of different color)
dd_5d = pd.read_csv(
    'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=U%2CG&ALDER=*', delimiter=';')
dd_5d = dd_5d.set_index('ALDER')
dd_5d = dd_5d.drop("I alt", axis=0).drop(columns="TID")
# print(dd_5d)

dd_married = dd_5d.loc[dd_5d['CIVILSTAND'] ==
                       'Gift/separeret']['INDHOLD']
# print(dd_married)

dd_unmarried = dd_5d.loc[dd_5d['CIVILSTAND'] ==
                         'Ugift']['INDHOLD']

# axis=0 is default (concats like sql UNION) axis=1 concats the data along the x axis
ts = pd.concat([dd_married, dd_unmarried], axis=1, keys=['Gift', 'Ugift'])

# ts.plot.bar()
ts.plot()
plt.show()
