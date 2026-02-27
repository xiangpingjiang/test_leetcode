# https://leetcode.cn/problems/sliding-window-maximum/  滑动窗口最大值
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque() # 单调队列 从左到右 严格降序，左边第一位始终最大
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans

s = Solution()
# s.maxSlidingWindow([3,1,4],3)

s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)