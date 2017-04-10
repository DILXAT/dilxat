class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        n = len(nums)
        nums.sort()  #进行排序
        if nums[0]!=0 :
            return 0
        elif nums[n-1]!=n:
            return n
        for i in range(n-1):
            if nums[i+1]!=nums[i]+1 :  #判定是否有序，当不等时将nums[i]+1输出，即为该组中不存在的数
                return nums[i]+1
