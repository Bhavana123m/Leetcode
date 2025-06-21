class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        # In snaparray we need to store index as key and list of (snap_id, val) in values as we are requesting get for index 
        # and snap_id
        self.snaparray = {}
        self.snap_id = 0
        for i in range(length):
            self.snaparray[i] = [(0,0)]   # initialize every index with [(0,0)] i.e., snap_id = 0 val = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index >= self.length:
            return
        self.snaparray[index].append((self.snap_id, val))  

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id+=1
        return self.snap_id-1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        list_snaps_index = self.snaparray[index]
        # print(list_snaps_index)
        left = 0
        right = len(list_snaps_index)-1
        while left<=right:
            mid = (left+right) // 2
            # print(mid)
            if list_snaps_index[mid][0] <= snap_id:
                left = mid+1
            else:
                right = mid-1
        # print(list_snaps_index[right])
        return list_snaps_index[right][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)