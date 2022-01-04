class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
                    
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
                
        count = 0
        curr = self.head.next
        
        while True:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next

    def addAtHead(self, val: int) -> None:
       
        new_node = ListNode(val)
        
        prev, succ = self.head, self.head.next
        
        self.size += 1
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        
        # because of the sentinel node
        prev, succ = self.tail.prev, self.tail
        
        self.size += 1
        
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
            
        if index > self.size:
            return 
         
        curr = self.head.next
        new_node = ListNode(val)
        count = 0
        
        while curr is not None:
            if count == index:
                prev, succ = curr.prev, curr
                new_node.next = succ
                new_node.prev = prev
                prev.next = new_node
                succ.prev = new_node

                self.size += 1 
                
                return
            
            count += 1
            curr = curr.next
                

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
                
        curr = self.head.next
        count = 0
        
        while curr is not None:
            if count == index:
                prev, succ = curr.prev, curr.next
                prev.next = succ
                succ.prev = prev
                self.size -= 1

                return
            
            count += 1
            curr = curr.next
        
        
        
    def show_element(self) -> None:
        curr = self.head.next
        array = []
        while curr.next is not None:
            array.append(str(curr.val))
            curr = curr.next
        
        print('->'.join(array))