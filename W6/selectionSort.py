# input 10 numbers
# output sorted numbers
# using selection sort
def main():
    # create a list
    numbers = []
    # input 10 numbers
    for i in range(10):
        numbers.append(eval(input("Enter a number: ")))
    # sort numbers
    selectionSort(numbers)
    # output sorted numbers
    print("The sorted numbers are: ", end="")
    for i in range(len(numbers)):
        print(numbers[i], end=" ")
    print()


def selectionSort(numbers):
    for i in range(len(numbers) - 1):
        # find the minimum in the numbers[i : len(numbers)]
        currentMin = numbers[i]
        currentMinIndex = i
        for j in range(i + 1, len(numbers)):
            if currentMin > numbers[j]:
                currentMin = numbers[j]
                currentMinIndex = j
        # swap numbers[i] with numbers[currentMinIndex] if necessary
        if currentMinIndex != i:
            numbers[currentMinIndex] = numbers[i]
            numbers[i] = currentMin


if __name__ == "__main__":
    main()
