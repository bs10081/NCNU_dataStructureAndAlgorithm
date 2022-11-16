import fileinput
# output StuID and Name


class student():
    def __init__(self, name, Chinese, English):
        self.name = name
        self.Chinese = Chinese
        self.English = English


def main():
    # input input_Chinese.txt
    input_file = []
    input_file = open("input_Chinese.txt", "r", encoding="utf-8")
    input_Chinese = input_file.readlines()

    selectionSort()


def selectionSort():
    # Sort
    for i in range(len(input_Chinese) - 1):
        minIndex = i
        for j in range(i + 1, len(input_Chinese)):
            if input_Chinese[j] < input_Chinese[minIndex]:
                minIndex = j
        input_Chinese[i], input_Chinese[minIndex] = input_Chinese[minIndex], input_Chinese[i]
    # output
    for i in range(len(input_Chinese)):
        print(input_Chinese[i], end="")


if __name__ == "__main__":
    main()
