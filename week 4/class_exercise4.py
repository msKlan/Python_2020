import numpy as np

filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(
    filename, delimiter=',', dtype=np.uint, skip_header=1)
print(type(bef_stats_df), ' of size: ', bef_stats_df.size)
# print('The skip_header=1 means that we have only the data\n\nfirst line:\n',
#       bef_stats_df[0], '\nlast line\n', bef_stats_df[len(bef_stats_df)-1])

dd = bef_stats_df
mask = (dd[:, 0] == 1998)  # for all rows filter column/index = 0 to be 1998
# print(dd[mask])

mask = (dd[:, 0] == 2015) & (dd[:, 2] == 18) & (dd[:, 3] == 5100)
# print(dd[mask])
# print(np.sum(dd[mask][:, 4]))

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}


def number_of_people_per_neighbourhood(n, mask):
    all_people_in_given_n = dd[mask & (dd[:, 1] == n)]
    # index 4 is no of 'PERSONER'
    sum_of_people = all_people_in_given_n[:, 4].sum()
    return sum_of_people


french_mask = (dd[:, 0] == 2015) & (dd[:, 3] == 5130)
german_mask = (dd[:, 0] == 2015) & (dd[:, 3] == 5180)

french = np.array([number_of_people_per_neighbourhood(
    n, french_mask) for n in neighb.keys()])
# print(french)
germans = np.array([number_of_people_per_neighbourhood(
    n, german_mask) for n in neighb.keys()])
# print(germans)

max_french_index = np.argmax(french)
max_germans_index = np.argmax(germans)

msg = 'The majority of {} {} are living in {}'
french_neighb_index = list(neighb.keys())[max_french_index]
# print(msg.format(french.max(), 'Frenchmen',
#                  neighb[max_french_index]))
# print(msg.format(germans.max(), 'Germans',
#                  neighb[list(neighb.keys())[max_germans_index]]))
