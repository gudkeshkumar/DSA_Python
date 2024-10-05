class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

class SinglyLinkedList:

    def __init__(self, head = None):
        self.head = head

    # Function to convert an array to linked list
    def arrayToLinkedList(self, arr):
        n = len(arr)
        if n == 0:
            return None

        head = ListNode(arr[0])
        cur = head
        for i in range(1,n):
            cur.next = ListNode(arr[i])
            cur = cur.next
        self.head = head
        return head

        
    #

def printLinkedList(head):
    current = head
    while current is not None:
        print(f"{current.val} ->", end = "")
        current = current.next
    print("None")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ll = SinglyLinkedList()
    # Convert array to linked list
    head = ll.arrayToLinkedList(arr)

    # Print the linked list
    printLinkedList(ll.head)
