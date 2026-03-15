# https://leetcode.com/problems/product-of-array-except-self/description

'''
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
'''
Inputs:
# nums = [-1,1,0,-3,3] 
# [0,0,9,0,0]

# nums = [1,2,3,4]
# [24,12,8,6]

# nums = [1,2,3,4,5]
#[120,60,40,30,24]
'''


'''
Solution 1 : BruteForce
class Solution:
    def productExceptSelf(self, nums):
        lnum = len(nums)
        arr = []
        # Calculating prefix array
        prefix_arr = [1]
        for i in range(1, lnum):
            cal = prefix_arr[i-1] * nums[i-1]
            prefix_arr.insert(i, cal)

        # return prefix_arr
        
        suffix_arr = [1] * lnum
        for i in range(lnum-2, -1, -1):
            cal = suffix_arr[i+1] * nums[i+1]
            # print(f"{i} : {cal}")
            suffix_arr[i] = cal

        # return suffix_arr
        
        for i in range(lnum):
            cal = prefix_arr[i] * suffix_arr[i]
            print(cal)
            arr.append(cal)
        
        return arr

obj = Solution()
print(obj.productExceptSelf(nums)) 

'''


# Solution 2 : Same array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lnum = len(nums)
        arr = [1] * lnum
        
        # nums = [1,2,3,4,5]
        # Calculating prefix array
        prefix = 1
        for i in range(lnum):
            arr[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(lnum-1, -1, -1):
            arr[i] = arr[i] * suffix
            suffix = suffix * nums[i]
            
        return arr
