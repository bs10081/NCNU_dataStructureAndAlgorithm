# 用物件導向的方式設計一個 Single Linked List, 然後產生一個物件, 產生一個介於(-50, 100)間的五個亂數, 依序用 物件.Append(亂數值) 的方法建立 Single Listed List, 然後印出[排序前資料], 再用 PrintList(), 將你的資料印出來, 接下來你要用 物件.Sort() 的方法將 Single Linked List 的資料排序(由小到大). 然後在印出[排序後資料], 接著再用 物件.PrintList()將你的資料印出來.
# 排序使用 Bubble Sort

print("學號: 110213027, 姓名: 簡齊君")


def main():
    # 產生一個介於(-50, 100)間的五個亂數
    import random
    list = [random.randint(-50, 100) for i in range(5)]
    # 依序用 物件.Append(亂數值) 的方法建立 Single Listed List
    s = SingleLinkedList()
    for i in list:
        s.append(i)
    # 然後印出 排序前資料...
    print("排序前資料...")
    # 再用 PrintList(), 將資料印出來
    s.printList()
    # 接下來用 物件.Sort() 的方法將 Single Linked List 的資料排序(由小到大)
    s.sort()
    # 然後在印出 排序後資料...
    print()
    print("排序後資料...")
    # 接著再用 物件.PrintList()將資料印出來.
    s.printList()
    print()

# 排序使用 Bubble Sort


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def printList(self):
        node = self.head
        while node is not None:
            # 同行輸出
            print(node.data, end=" ")
            node = node.next

    def sort(self):
        node = self.head
        while node is not None:
            node2 = node.next
            while node2 is not None:
                if node.data > node2.data:
                    node.data, node2.data = node2.data, node.data
                node2 = node2.next
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    main()
