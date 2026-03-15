'''
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
'''

# nums = [1,0,1,2] # 3
# nums = [100,4,200,1,3,2] # 4
# nums = [0,3,7,2,5,8,4,6,0,1]  # 9
'''
Solution 1 : BruteForce
class Solution:
    def longestConsecutive(self, nums):
        if len(nums) < 1:
            return 0
        
        nums.sort()
        count = 1
        max_count = float('-inf')
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i+1] - nums[i] == 1:
                count += 1
            else:
                count = 1
            
            if count > max_count:
                max_count = count
        
        return max_count


obj = Solution()
print(obj.longestConsecutive(nums))
'''

'''
Solution 2
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                next_num = num+1
                count = 1
                while next_num in nums:
                    next_num = next_num + 1
                    count += 1
                
                longest = max(longest, count)
        
        return longest


# nums = [1,0,1,2] # 3
# nums = [100,4,200,1,3,2] # 4
nums = [0,3,7,2,5,8,4,6,0,1]  # 9
obj = Solution()
print(obj.longestConsecutive(nums))
'''