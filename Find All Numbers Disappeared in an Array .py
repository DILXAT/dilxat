class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        n = len(nums)
        a=[]
        for i in range(n):
            value = abs(nums[i])-1
            if(nums[value]>0):
                nums[value]=-nums[value]
        for i in range(n):
            if(nums[i]>0):
                a.append(i+1)
        
        return a
