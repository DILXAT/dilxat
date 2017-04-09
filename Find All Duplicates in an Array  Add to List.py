class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        b=[]
       
        for i in nums:
            if nums[abs(i)-1]<0:    #负数标识，在有数第二次出现时识别并加入b数组
                b.append(abs(i))
            else:
                nums[abs(i)-1] *= -1     #进行标识
                
                
                
        return b
