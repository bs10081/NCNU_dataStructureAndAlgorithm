# 亂數產生10個介於(-100~100)的整數，並將其存入串列中
# 用遞迴的方式找出串列中的最小值(用 min 表示)
# 並將最小值印出來
import random
print("學號: 110213027, 姓名: 簡齊君")

# 主程式


def main():
    # 亂數產生10個介於(-100~100)的整數，並將其存入串列中
    list = [random.randint(-100, 100) for i in range(10)]
    # 輸出原始資料 (格式: 原始資料: {list})
    print("原始資料: ", *list)
    # 用遞迴的方式找出串列中的最小值(用 min 表示)
    min = findMin(list)
    # 並將最小值印出來 (格式: 最小值: {min})
    print("最小值: ", min)

# 找出最小值


def findMin(list):
    if len(list) == 1:
        return list[0]
    else:
        return min(list[0], findMin(list[1:]))


if __name__ == '__main__':
    main()
