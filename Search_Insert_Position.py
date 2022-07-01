nums = [1,2,3,4,6,7,8,9]
target = 10
high = len(nums)-1
low = 0
        
def binarySearch (nums, low, high, target):
    mid = low + (high-low)//2
    if high < low : 
        return low -1
    if nums[mid] == target:
        return mid 
    elif target < nums[mid]:
        return binarySearch(nums,low, mid-1,target)
    else :
        return binarySearch(nums, mid+1, high, target)
            
print(binarySearch(nums, low, high, target))   

#########################################################################
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        def binarySearch (nums, low, high, target):
            mid = low + (high-low)//2
            if high < low : 
                return low 
            if nums[mid] == target:
                return mid 
            elif target < nums[mid]:
                return binarySearch (nums,low, mid-1,target)
            else :
                return binarySearch (nums, mid+1, high, target)
        
        return binarySearch(nums, low, high, target)
'''
#####################################################################ZZ
ZZ

