class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def arrayToLinkedList(self, arr):
        n = len(arr)
        if n == 0:
            return None

        head = Node(arr[0])
        head.prev = None
        cur = head

        for i in range(1, n):
            cur.next = Node(arr[i], prev= cur)
            cur = cur.next
        self.head = head
        return head

    def deleteHead(self, head):

        if head is None or head.next is None:
            return None

        head = head.next
        head.prev = None
        self.head = head
        return head

    def deleteTail(self, head):
        if head is None or head.next is None:
            return None

        current = head
        while current.next is not None:
            current = current.next
        
        current.prev.next = None
        return head


def printLinkedList(head):
    current = head
    while current is not None:
        print(f"{current.val} <->", end="")
        current = current.next
    print("None")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ll = DoublyLinkedList()
    ll.arrayToLinkedList(arr)
    # Convert array to linked list
    ll.deleteTail(ll.head)

    # Print the linked list
    printLinkedList(ll.head)
