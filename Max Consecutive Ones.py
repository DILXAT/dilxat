class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        a=[]
        for i in range(n):
            if(nums[i]):
                count+=1
                a.append(count)
            else:
                count = 0
                a.append(count)
        return max(a)
                
