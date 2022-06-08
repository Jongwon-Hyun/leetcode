class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.cap = k
        self.head = None
        self.tail = None
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.head is None and self.tail is None:
            self.queue[0] = value
            self.head = 0
            self.tail = 0
        elif self.tail == self.cap - 1:
            self.queue[0] = value
            self.tail = 0
        else:
            self.queue[self.tail + 1] = value
            self.tail += 1
        
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.queue[self.head] = None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == self.cap - 1:
            self.head = 0
        else:
            self.head += 1
        
        return True
        

    def Front(self) -> int:
        return self.queue[self.head] if self.head is not None else -1

    def Rear(self) -> int:
        return self.queue[self.tail] if self.tail is not None else -1
        

    def isEmpty(self) -> bool:
        return self.head is None and self.tail is None
        

    def isFull(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.cap - 1 and self.tail == self.head - 1:
            return True
        elif self.tail == self.cap - 1 and self.head == 0:
            return True
        elif self.head - 1 == self.tail:
            return True
        
        return False
    
     # 4 7 2 5
     #   h    
     # t    

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()