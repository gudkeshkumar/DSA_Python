
class Solution:
    def leaders(self, nums):
        ans = []
        if not nums:
            return ans
        maxi = nums[-1]
        ans.append(maxi)
        for i in range(len(nums) -2, -1, -1):
            if nums[i] > maxi:
                maxi = nums[i]
                ans.append(maxi)



        ans.reverse()
        return ans