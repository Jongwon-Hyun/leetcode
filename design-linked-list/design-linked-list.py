class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
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
        if self.size == 0:
            node.prev, node.next = None, None
        else:
            node.prev, node.next, self.head.prev = None, self.head, node
            
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            node = Node(val)
            tail_node = self.__findNode(self.size - 1)
            tail_node.next, node.prev, node.next = node, tail_node, None
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size: 
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            index_node = self.__findNode(index)
            if index_node is None:
                return

            node = Node(val)
            node.prev, node.next = index_node.prev, index_node
            index_node.prev.next, index_node.prev = node, node
            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index:
            return
        if index == 0:
            if self.head.next:
                self.head.next.prev, self.head = None, self.head.next
            else:
                self.head = None
            self.size -= 1
        else:
            find_node = self.__findNode(index)
            if find_node is None:
                return
            
            if find_node.next:
                find_node.prev.next, find_node.next.prev = find_node.next, find_node.prev
            else:
                find_node.prev.next = None
              
            self.size -= 1
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)