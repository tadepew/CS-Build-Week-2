class Solution:
    def containsDuplicates(self, nums):
        # set keeps track of numbers already in array
        visited = set()
        
        # iterate through list
        for num in nums:
            
            # if num in set, then there is a duplicate
            if num in visited:
                #so return true
                return True
            # if the num isn't in set, add it
            else:
                visited.add(num)
                
        # no dups
        return False
