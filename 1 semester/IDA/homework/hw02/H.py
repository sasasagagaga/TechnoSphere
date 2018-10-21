from collections import deque


class BinarySearchTree :
    def __init__(self, val=None):
        self.left = self.right = None
        self.val = val
    
    def append(self, val):
        if self.val is None:
            self.val = val
            return
        if self.val > val:
            if self.left is None:
                self.left = BinarySearchTree(val)
            else:
                self.left.append(val)
        else:
            if self.right is None:
                self.right = BinarySearchTree(val)
            else:
                self.right.append(val)
    
    def __contains__(self, val):
        if self.val is None:
            return False
        if self.val == val:
            return True
        if self.val > val:
            if self.left is None:
                return False
            return val in self.left
        if self.right is None:
            return False
        return val in self.right

    def __iter__(self):
        self.d = deque()
        if self.val is not None:
          self.d.append(self)
        return self
    
    def __next__(self):
        if len(self.d) == 0:
            raise StopIteration
        ret = self.d.popleft()
        if ret.left is not None:
            self.d.append(ret.left)
        if ret.right is not None:
            self.d.append(ret.right)
        return ret.val
