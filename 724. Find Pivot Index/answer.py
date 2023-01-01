class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        return -1
      
    '''
    not eficent but detail code 
    class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        length=len(nums)
        for i in range(length):
            left,right=0,0
            for j in range(i):
                left=nums[j]+left
            for p in range(i+1,length):
                right=nums[p]+right
            print(left,right)
            if left==right:
                return i
            
        return -1'''
