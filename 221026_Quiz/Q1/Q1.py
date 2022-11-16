import random
# output StuID and Name


def main():
    # create a 6 lenght list
    numbers = []
    # Generate five random integers from the integers 50 to 60.
    for i in range(6):
        numbers.append(random.randint(50, 60))
        # If it is repeated with the list, a new random number will be generated again
        while numbers[i] in numbers[:i]:
            numbers[i] = random.randint(50, 60)
    # add StuiD last 2 number
    numbers.append(27)
    # sort numbers
    insertionSort(numbers)


def insertionSort(numbers):
    for i in range(1, len(numbers)):
        # insert numbers[i] into a sorted sublist numbers[0 : i] so that
        # numbers[0 : i + 1] is sorted
        currentElement = numbers[i]
        k = i - 1
        while k >= 0 and numbers[k] > currentElement:
            numbers[k + 1] = numbers[k]
            k -= 1
        numbers[k + 1] = currentElement
        # output sorted numbers
        print("第", i, "次排序結果: ", numbers)


if __name__ == "__main__":
    main()
