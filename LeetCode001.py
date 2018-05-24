#LeetCode 001
#考点：数组
'''
001 Two Sum
Given an array of integers, return indices(索引) of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = {};#使用字典存储遍历过的num和对应下标{num:index}
        length = len(nums);#计算输入的列表长度
        for i in range(length):
            #如果target-当前num的差在arr中，则表示已经找到答案，返回结果即可
            if (target - nums[i]) in arr:
                return [arr[target - nums[i]], i];
            arr[nums[i]] = i;#否则，将该num及其下标存入arr中
