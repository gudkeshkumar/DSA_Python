from SLinkedList import ListNode

class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def arrayToCircularLinkedList(self, arr):
        n = len(arr)
        if n == 0:
            return None

        head = ListNode(arr[0])
        cur = head
        for i in range(1, n):
            cur.next = ListNode(arr[i])
            cur = cur.next
        cur.next = head
        self.head = head
        return head
    
    def addFirst(self, val):
        newNode = ListNode(val)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head
            self.head = newNode
            
    def addLast(self, val):
        newNode = ListNode(val)
        if self.head is None:
            self.addFirst(val)
        else:
            cur  = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head

    def searchNode(self, val):

        if head is None:
            return False

        temp = self.head

        while True:

            if temp.val == val:
                return True
            temp = temp.next

            if temp == head:
                break

        return False

    def deleteNode(self, val):

        if self.head is None:
            return

        if self.head.next == self.head and self.head.val == val:
            self.head = None

        elif self.head.val == val:
            lastNode = self.head
            while lastNode.next != self.head:
                lastNode = lastNode.next
            lastNode.next = self.head.next
            self.head = self.head.next

        else:

            current = self.head

            while current.next != self.head:

                if current.next.val == val:
                    current.next = current.next.next
                    break
                current = current.next



            
            
    
            
            
            
            
            
            
            
            
            
            
            

def printCircularLinkedList(head):
    if not head:
        return
    current = head
    while True:
        print(f"{current.val} ->", end="")
        current = current.next
        if current == head:
            break

    print(f"{current.val}")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ll = CircularLinkedList()
    # Convert array to linked list
    head = ll.arrayToCircularLinkedList(arr)
    # ll.addLast(6)
    # print(ll.searchNode(6))
    # ll.deleteNode(3)

    # Print the linked list
    printCircularLinkedList(ll.head)
