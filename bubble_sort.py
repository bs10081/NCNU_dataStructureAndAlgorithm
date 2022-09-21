# generate a random integer between 10 ~ 20 as the length of the data array
# fill the content of the data using the random integer between -50 ~ 50
# Use the bubble sort algorithm to sort and print the results of each round of sorting

import random


def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print(data)
    return data


def main():
    bubble_sort([random.randint(-50, 50)
                for i in range(random.randint(10, 20))])


if __name__ == '__main__':
    main()
