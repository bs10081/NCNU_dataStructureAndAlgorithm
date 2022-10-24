# input 10 num
# output sorted num
# using insertion sort
def main():
    # create a list
    numbers = []
    # input 10 numbers
    for i in range(10):
        numbers.append(eval(input("Enter a number: ")))
    # sort numbers
    insertionSort(numbers)
    # output sorted numbers
    print("The sorted numbers are: ", end="")
    for i in range(len(numbers)):
        print(numbers[i], end=" ")
    print()


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


if __name__ == "__main__":
    main()
