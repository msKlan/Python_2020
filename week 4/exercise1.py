import numpy as np
import matplotlib.pyplot as plt

filename = './befkbhalderstatkode.csv'
dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}


def number_of_people_per_neighbourhood(n, mask):
    all_people_in_given_n = dd[mask & (dd[:, 1] == n)]
    # index 4 is no of 'PERSONER'
    sum_of_people = all_people_in_given_n[:, 4].sum()
    return sum_of_people


def print_how_many_lived_where_in_2015():
    mask3 = (dd[:, 0] == 2015)
    for key, value in neighb.items():
        print("In 2015 %s people lived in %s" %
              (number_of_people_per_neighbourhood(key, mask3), value))


# print_how_many_lived_where_in_2015()   # Exercise 1.3


def getSumPerNeighb(year):
    lst = {}
    for key, value in neighb.items():
        lst.update(
            {value: np.sum(dd[(dd[:, 0] == year) & (dd[:, 1] == key)][:, 4])})
    return lst


def plotSizeOfCityArea():
    x = []
    y = []
    sortedNeighb = sorted(getSumPerNeighb(2015).items(), key=lambda x: x[1])
    # print(sortedNeighb)
    for key, value in sortedNeighb:
        x.append(key)
        y.append(value)
    # plt.figure(figsize=(5, 8))
    plt.bar(x, y, width=0.5, linewidth=0, align='center')
    plt.title("Size of each city area from the smallest to the largest", fontsize=10)
    plt.xticks(x, rotation=45, fontsize=8)
    plt.show()

# plotSizeOfCityArea()  # Exercise 1.4


def printHowManyInCopenhagenIn2015Above65():
    mask = (dd[:, 0] == 2015) & (dd[:, 2] > 65)
    return np.sum(dd[mask][:, 4])

# print(printHowManyInCopenhagenIn2015Above65())  # Exercise 1.5


def printHowManyInCopenhagenIn2015Above65NordicNotDK():
    mask = (dd[:, 0] == 2015) & (dd[:, 2] > 65) & ((dd[:, 3] == 5104) | (
        dd[:, 3] == 5106) | (dd[:, 3] == 5110) | (dd[:, 3] == 5120))
    return np.sum(dd[mask][:, 4])


# print(printHowManyInCopenhagenIn2015Above65NordicNotDK())  # Exercise 1.6


def plotChangesOfNumberOfPeopleInVesterbroAndOsterbroFrom1992to2015():
    x = []
    yVest = []
    yOest = []

    for year in list(range(1992, 2015)):
        x.append(year)
        yVest.append(np.sum(dd[(dd[:, 0] == year) & (dd[:, 1] == 2)][:, 4]))
        yOest.append(np.sum(dd[(dd[:, 0] == year) & (dd[:, 1] == 4)][:, 4]))

    # # plt.figure(figsize=(5, 6))
    # plt.bar(x, y, width=0.5, linewidth=0, align='center')
    # plt.title("Size of each city area from the smallest to the largest", fontsize=10)

    plt.plot(x, yVest, label="Vesterbro/Kgs.")
    plt.plot(x, yOest, label="Østerbro")

    # plt.xticks(x, rotation=45, fontsize=8)
    plt.legend()
    plt.show()


plotChangesOfNumberOfPeopleInVesterbroAndOsterbroFrom1992to2015()  # Exercise 1.7
