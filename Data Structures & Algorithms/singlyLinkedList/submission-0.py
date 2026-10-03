class LinkedList:

    class Node:
        def __init__(self, n: int):
            self.val = n
            self.next = None
    
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        i = 0
        curr = self.head
        while i < index:
            curr = curr.next
            i += 1
        return curr.val

    def insertHead(self, val: int) -> None:
        n = self.Node(val)
        n.next = self.head
        self.head = n
        if self.size in (0, 1):
            self.tail = n
        self.size += 1

    def insertTail(self, val: int) -> None:
        self.tail.next = self.Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        i = 0
        dum = self.Node(None)
        dum.next = self.head
        curr = dum
        while i < index:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        self.size -= 1
        return True
        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
        
