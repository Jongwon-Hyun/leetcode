class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
    
    def __findNode(self, index: int) -> Node:
        if index > self.size - 1 or index < -self.size:
            return None
        
        if self.head is None:
            return None
        
        if index < 0:
            index += self.size
        
        cursor_node = self.head  
        for _ in range(index):
            cursor_node = cursor_node.next 
         
        return cursor_node

    def get(self, index: int) -> int:
        node = self.__findNode(index)
        if node is None:
            return -1
        
        return node.val
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            node = Node(val)
            tail_node = self.__findNode(self.size - 1)
            tail_node.next = node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            prev_node = self.__findNode(index - 1)
            if prev_node is None:
                return
            
            node = Node(val)
            node.next = prev_node.next
            prev_node.next = node
            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            node = self.head
            self.head = node.next
            node = None
            self.size -= 1
        else:
            prev_node = self.__findNode(index - 1)
            node = self.__findNode(index)
            if node is None:
                return
     
            prev_node.next = node.next
            node = None
            self.size -= 1
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)