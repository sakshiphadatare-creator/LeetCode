class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        self.rtype = {}
        for current_index, i in enumerate(nums):
            #current_index = nums.index(i)
            complement = target - i
        
            if complement in self.rtype:
                return [self.rtype[complement], current_index]
                #nums.index(i) ,nums.index(complement)
            
            self.rtype[i] = current_index
            #self.rtype[i] = nums.index(i)


class1 = Solution()
print(class1.twoSum([3,3],6))



    
    
        
        