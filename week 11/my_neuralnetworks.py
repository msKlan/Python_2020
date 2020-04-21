import matplotlib.pyplot as plt
import numpy as np
# from my_modules import webget
import csv
from my_nn_utils1 import predict, inputs


filename = './simple_digit_trainingset.csv'


def read_data(filename):
    data = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            label = reader.line_num - 1
            image = np.array(row[:], dtype=np.int8)
            data.append((label, image))
    return data


def generate_plot(data):
    count = 0
    f = plt.figure(figsize=(10, 5))
    for idx, row in enumerate(data):
        imarray = row[1].reshape((5, 5))
        plt.subplot(2, 5, idx + 1)
        plt.subplots_adjust(hspace=0.5)
        count += 1
        plt.title('Label = {}'.format(row[0]))
        plt.imshow(imarray, cmap='Greys', interpolation='None')
    return plt


# Exploring the values of np.exp
print('high positive', np.exp(10))
print('1 positive', np.exp(1))
print('0 ', np.exp(0))
print('1 negative', np.exp(-4))


def plot_testset(data):
    count = 0
    f = plt.figure(figsize=(10, 5))
    data = np.array(data)
    for idx, row in enumerate(data):
        imarray = row.reshape((5, 5))
        plt.subplot(2, len(data), idx + 1)
        plt.subplots_adjust(hspace=0.5)
        count += 1
        plt.imshow(imarray, cmap='Greys', interpolation='None')
    return plt


test_set = [[0, 1, 1, 1, 0,
             0, 0, 0, 1, 1,
             0, 0, 1, 1, 0,
             0, 0, 0, 1, 1,
             0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0,
             1, 0, 0, 1, 1,
             0, 1, 1, 1, 0,
             1, 0, 0, 1, 1,
             0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 1, 0, 0]]
print(test_set)
plt.show(plot_testset(test_set))

for test_data in test_set:
    result = predict(test_data)
    result = np.array(result)
    print(np.argmax(result), np.array_str(
        result, precision=2, suppress_small=True))

for test_data in inputs:
    result = predict(test_data)
    result = np.array(result)
    print(np.argmax(result), np.array_str(
        result, precision=2, suppress_small=True))
