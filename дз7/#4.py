class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def get(self, index):
        if index >= self.len:
            return
        current = self.head
        for i in range(index):
            current = current.next
        return current.value
    
    def len(self):
        return self.len
    
    def contains(self, value):
        k = 0
        for i in range(self.len):
            if self.get_node(i).value == value:
                k += 1
        if k == 0:
            return False
        else:
            return True
        
    def delete(self, index):
        if self.len == 0:
            return        
        if index >= self.len and self.len > 0:
            return
        elif self.len == 1:
            self.head = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.len - 1:
            kill_node = self.get_node(self.len - 1)
            n_prev = self.get_node(self.len - 2)
            kill_node.prev = None
            n_prev.next = None
        else:
            kill_node = self.get_node(index)
            n_prev = self.get_node(index-1)
            n_next = self.get_node(index+1)
            n_prev.next = n_next
            n_next.prev = n_prev
            kill_node.next = None
            kill_node.prev = None
        self.len -= 1
        
    def insert(self, new, index):
        if index > self.len:
            return
        else:       
          new_node = Node(new)
          if self.head is None:
            self.head = new_node
            self.len += 1
          elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.len += 1
          elif index == self.len:
            new_node.prev = self.get_node(self.len-1)
            self.get_node(self.len-1).next = new_node
            self.len += 1
          else:
            cur_node = self.get_node(index)
            prev_node = self.get_node(index-1)
            new_node.next = cur_node
            cur_node.prev = new_node
            new_node.prev = prev_node
            prev_node.next = new_node
            self.len += 1   


