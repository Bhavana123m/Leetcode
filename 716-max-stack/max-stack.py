import heapq  # Python's heapq is a min-heap; we'll push negatives to simulate max-heap

class _Node(object):
    """Doubly-linked list node to store each stack element."""
    def __init__(self, val, idx):
        self.val = val      # value of the element
        self.idx = idx      # unique increasing id to break ties for duplicates
        self.prev = None    # previous node in DLL
        self.next = None    # next node in DLL
        self.alive = True   # alive flag for lazy deletion

class MaxStack(object):

    def __init__(self):
        # Create head/tail sentinels for DLL
        self.head = _Node(0, -1)
        self.tail = _Node(0, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        # Max-heap storing (-val, -id, node)
        self.heap = []

        # Counter to assign unique increasing ids
        self.counter = 0

    def _dll_append(self, node):
        """Append node before the tail (stack top)."""
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def _dll_remove(self, node):
        """Remove a node from DLL in O(1)."""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _heap_clean(self):
        """Discard dead nodes from the top of the heap lazily."""
        while self.heap and not self.heap[0][2].alive:
            heapq.heappop(self.heap)

    def push(self, x):
        """
        Push element x onto the stack.
        O(log n) because of heap push.
        """
        node = _Node(x, self.counter)
        self.counter += 1
        # Add to DLL (stack top)
        self._dll_append(node)
        # Add to heap (negative for max behavior)
        heapq.heappush(self.heap, (-x, -node.idx, node))

    def pop(self):
        """
        Remove the element on top of the stack and return it.
        O(1).
        """
        node = self.tail.prev
        self._dll_remove(node)
        node.alive = False   # mark as dead for heap
        return node.val

    def top(self):
        """
        Get the element on the top without removing it.
        O(1).
        """
        return self.tail.prev.val

    def peekMax(self):
        """
        Retrieve the maximum element without removing it.
        O(log n) amortized.
        """
        self._heap_clean()
        return self.heap[0][2].val

    def popMax(self):
        """
        Retrieve and remove the top-most maximum element.
        O(log n) amortized.
        """
        self._heap_clean()
        _, _, node = heapq.heappop(self.heap)
        self._dll_remove(node)
        node.alive = False
        return node.val
    


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()