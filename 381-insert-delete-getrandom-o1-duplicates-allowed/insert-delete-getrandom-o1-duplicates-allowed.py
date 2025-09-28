class RandomizedCollection(object):

    def __init__(self):
        # Dynamic array to hold all elements, including duplicates
        self.arr = []
        # Hash map: value -> set of indices in self.arr where this value occurs
        self.pos = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # Check if val already existed (non-empty set in pos)
        existed = val in self.pos and len(self.pos[val]) > 0

        # If not existed before, initialize its set
        if not existed:
            self.pos.setdefault(val, set())

        # Add the new index (tail of arr) into the set of positions
        self.pos[val].add(len(self.arr))

        # Append the value itself into the array
        self.arr.append(val)

        # Return True if this was the first time we saw val
        return not existed
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # If val absent or set empty, nothing to remove
        if val not in self.pos or not self.pos[val]:
            return False

        # Get an arbitrary index where val occurs (e.g., pop one element from the set)
        idx = self.pos[val].pop()

        # Identify the last index and last value in the array
        last_idx = len(self.arr) - 1
        last_val = self.arr[last_idx]

        # If the element to remove is not the last one, swap
        if idx != last_idx:
            # Move the last element into idx
            self.arr[idx] = last_val

            # Update last_val's index set:
            # remove its old index (last_idx) and add the new index (idx)
            self.pos[last_val].remove(last_idx)
            self.pos[last_val].add(idx)

        # Remove the last element from the array
        self.arr.pop()

        # Optional: clean up empty set for val
        # if not self.pos[val]:
        #     del self.pos[val]

        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        # Choose a random index uniformly from the array
        return self.arr[random.randint(0, len(self.arr) - 1)]
        # Or simpler: return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()