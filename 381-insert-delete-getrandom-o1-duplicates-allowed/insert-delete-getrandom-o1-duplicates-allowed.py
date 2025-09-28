class RandomizedCollection(object):

    def __init__(self):
        self.hashset = collections.defaultdict(set)
        self.nums = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashset:
            self.nums.append(val)
            self.hashset[val].add(len(self.nums) - 1)
            return False
        else:
            self.nums.append(val)
            self.hashset[val].add(len(self.nums) - 1)
            return True

        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashset:
            return False
        
        lastElement = self.nums[-1]
        index = self.hashset[val].pop()

        self.nums[index] = lastElement

        self.hashset[lastElement].add(index)
        self.hashset[lastElement].remove(len(self.nums) - 1)
        self.nums.pop()

        if not self.hashset[val]:
            del self.hashset[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)