# 用 array 模擬 Stack 的資料結構(MaxSize = 8)
# 1 代表 push, 2 代表 pop, 3 代表 由上至下印出 stack 並印出 top 值
# 數字後面的字元代表 push 或 pop 的值
import array

stack = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
top = -1
MaxSize = 8


def main():
    # 輸入一行字串
    line = input("請輸入一行字串: ")
    # 將字串中的數字及字母分別取出
    num = [int(i) for i in line if i.isdigit()]
    char = [i for i in line if i.isalpha()]
    # 依序執行指令
    for i in range(len(num)):
        if num[i] == 1:
            push(char[i])
        elif num[i] == 2:
            pop()
        elif num[i] == 3:
            printStack()
        else:
            print("Error")


def push(char):
    global top
    if top == MaxSize - 1:
        print("Stack is full")
    else:
        top += 1
        stack[top] = char
        print("Push", char)


def pop():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("Pop", stack[top])
        top -= 1


def printStack():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack: ", end="")
        for i in range(top, -1, -1):
            print(stack[i], end=" ")
        print("Top:", stack[top])


if __name__ == '__main__':
    main()
