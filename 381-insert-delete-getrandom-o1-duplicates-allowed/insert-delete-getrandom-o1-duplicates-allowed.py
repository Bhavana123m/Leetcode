import random  # import the random module to generate random integers
# we avoid fancy builtins like next, zip, bisect as requested
# we also avoid relying on random.choice to show the index-based method explicitly

class RandomizedCollection(object):
    def __init__(self):
        # dynamic array storing every element instance (duplicates occupy multiple slots)
        self.arr = []
        # dictionary mapping value -> set of indices where it appears in self.arr
        # using a plain dict of sets to keep it explicit
        self.pos = {}

    def insert(self, val):
        # determine the index where the new value will be placed (end of array)
        idx = len(self.arr)
        # append the value to the array
        self.arr.append(val)

        # if val not in pos yet, create a new set for its indices
        if val not in self.pos:
            self.pos[val] = set()
            # record the new index
            self.pos[val].add(idx)
            # since it's the first time this value appears, return True
            return True
        else:
            # record the new index in the existing set
            self.pos[val].add(idx)
            # value existed before this insert, so return False
            return False

    def remove(self, val):
        # if val not present at all, or its index set is empty, we cannot remove it
        if val not in self.pos or len(self.pos[val]) == 0:
            return False

        # take any index for this value from its set using pop()
        # pop() both retrieves and removes an arbitrary element from the set in O(1) average time
        remove_idx = self.pos[val].pop()

        # compute the last index and the last value in the array
        last_idx = len(self.arr) - 1
        last_val = self.arr[last_idx]

        # if the element to remove is not the last one, we need to move the last into its place
        if remove_idx != last_idx:
            # place last_val into the position remove_idx
            self.arr[remove_idx] = last_val

            # update the index set for last_val:
            # 1) remove the old index (last_idx) because last_val is no longer at the end
            # 2) add the new index (remove_idx) where last_val has been moved
            # ensure last_val has a set in the dictionary (it always should)
            # remove last_idx from last_val's set if it exists there
            if last_val in self.pos:
                # we need to remove last_idx; check membership to be safe
                if last_idx in self.pos[last_val]:
                    self.pos[last_val].remove(last_idx)
                # add the new index where last_val now resides
                self.pos[last_val].add(remove_idx)
            else:
                # in normal flow this branch should not happen, but for safety:
                self.pos[last_val] = set()
                self.pos[last_val].add(remove_idx)

        # now remove the last element from the array (either it was the target or we moved it)
        self.arr.pop()

        # if after removal the set of indices for val became empty, clean it up from the dictionary
        if len(self.pos[val]) == 0:
            del self.pos[val]

        # removal succeeded
        return True

    def getRandom(self):
        # compute the number of elements currently stored
        n = len(self.arr)
        # generate a random integer in [0, n-1]
        r = random.randint(0, n - 1)
        # return the element at that index
        return self.arr[r]
