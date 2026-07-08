class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        self.rtype = {}
        for idx, val in enumerate(nums):
            #idx = nums.index(val)
            complement = target - val
        
            if complement in self.rtype:
                return [self.rtype[complement], idx]
                #nums.index(i) ,nums.index(complement)
            
            self.rtype[val] = idx
            #self.rtype[i] = nums.index(i)


class1 = Solution()
print(class1.twoSum([3,3],6))



    
    
        
        