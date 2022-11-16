

def main():
    # 讀入包含八種狗狗的檔案(input.txt), 包含 狗狗名稱, 體重排行(小到大代表輕到重), 智商排行(小到大代表聰明到笨), 並且以空白分隔, 第一行為標題
    data = []
    with open("input.txt", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split())
    # 建立一個字典, key 為狗狗名稱, value 為一個 list, 包含 體重排行, 智商排行
    dog = {}
    for i in range(1, len(data)):
        dog[data[i][0]] = [int(data[i][1]), int(data[i][2])]

    # 輸出讀檔結果及魅力值
    print("讀檔結果:")
    print("狗狗名稱 體重排行 智商排行 魅力值")
    for i in range(1, len(data)):
        print(data[i][0], data[i][1], data[i][2],
              charismaFormula(dog[data[i][0]]), end=" ")
        print()
    print()

    # 先印出原始體重
    print("體重排序原始陣列內容:")
    for i in range(1, len(data)):
        print(data[i][0], data[i][1], end=" ")
    print()
    # 對體重由小到大,左到右做bubble sort,
    print("體重排序結果:")
    bubbleSort(data)
    print()

    # 印出原始智商
    print("智商排序原始陣列內容:")
    for i in range(1, len(data)):
        print(data[i][0], data[i][2], end=" ")
    print()
    # 對智商由小到大,左到右做Selection sort
    print("智商排序結果:")
    SelectionSort(data)
    print()

    # 印出原始魅力值
    print("魅力值排序原始陣列內容:")
    for i in range(1, len(data)):
        print(data[i][0], charismaFormula(dog[data[i][0]]), end=" ")
    print()

    # 對魅力值由小到大,左到右做Insertion sort
    print("魅力值排序結果:")
    for i in range(1, len(data)):
        for j in range(i, len(data)):
            if charismaFormula(dog[data[j][0]]) < charismaFormula(dog[data[i][0]]):
                data[i], data[j] = data[j], data[i]
        print("第", i, "回合排序後魅力值排序:")
        for k in range(1, len(data)):
            print(data[k][0], charismaFormula(dog[data[k][0]]), end=" ")
        print()


def SelectionSort(data):
    # 選擇排序法, 印出每一次排序結果, 排序完就退出
    for i in range(1, len(data)):
        for j in range(i, len(data)):
            if int(data[j][2]) < int(data[i][2]):
                data[i], data[j] = data[j], data[i]
        print("第", i, "回合排序後智商排序:")
        for k in range(1, len(data)):
            print(data[k][0], data[k][2], end=" ")
        print()


def bubbleSort(data):
    # 氣泡排序法, 印出每一次排序結果, 排序完就退出
    for i in range(1, len(data)):
        for j in range(1, len(data) - i):
            if int(data[j][1]) > int(data[j + 1][1]):
                data[j], data[j + 1] = data[j + 1], data[j]
        print("第", i, "回合排序後體重排序:")
        for k in range(1, len(data)):
            print(data[k][0], data[k][1], end=" ")
        print()


def charismaFormula(dog):
    # 計算魅力值, 魅力值 = (8 - 體重排行 ) +  (8 - 智商排行)
    # 吉娃娃魅力為 0
    return 0 if dog[0] == 1 else (8 - dog[0]) + (8 - dog[1])


if __name__ == '__main__':
    main()
