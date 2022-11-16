import random


def main():
    # 建立大小為4的陣列,內容為3,5,7,9
    a = [3, 5, 7, 9]
    # 產生一個 0 到 3 的隨機數
    i = random.randint(0, 3)
    # 隨機數作為 a 的 index,取出 a[index] 的值 為 魔方陣大小
    n = a[i]
    print("魔方陣大小為", n)
    magicSquare(n)

# 魔方陣函式, 把 1 放在第一列的中間,然後往左上方填入數字,如果超出邊界,則從另一邊繼續填入,如果該位置已經有數字,則在原始位置正下方一格填入,直到填滿, 如果數字為個位數, 則格式化成兩位數, 例如 1 -> 01


def magicSquare(n):
    # 建立大小為 n*n 的陣列,內容為 0
    a = [[0 for i in range(n)] for j in range(n)]
    # 設定初始位置
    row = 0
    col = n // 2
    # 依序填入數字
    for i in range(1, n * n + 1):
        # 如果該位置已經有數字,則直接往正下方一格填入
        if a[row][col] != 0:
            row += 2
            col += 1
        # 如果超出邊界,則從另一邊繼續填入
        if row < 0:
            row = n - 1
        if row >= n:
            row = 0
        if col < 0:
            col = n - 1
        if col >= n:
            col = 0
        # 填入數字
        a[row][col] = i
        # 設定下一個位置
        row -= 1
        col -= 1
    # 輸出魔方陣
    for i in range(n):
        for j in range(n):
            print("%02d" % a[i][j], end=" ")
        print()


if __name__ == '__main__':
    main()
