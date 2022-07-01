
def removeDuplicates( nums):
        length = len(nums)
        nums = list(set(nums))
        new_length = len(nums)
        diff = length - new_length
        x = "*"
        
        for i in range(diff):
            nums.append(x)
            
        return new_length, nums

nums = [1,1,2,3,3,4,4,5,6,6,6]
nums[1:5] = ["hello"]
print(len(nums) , nums)
#print(removeDuplicates(nums))