class Solution:
    # Longest Consecutive Sequence in an Array

    # Given an array nums of n integers, return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.
    # Example 1
    # Input: nums = [100, 4, 200, 1, 3, 2]
    # Output: 4
    # Explanation: The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4.
    # This sequence can be formed regardless of the initial order of the elements in the array.

    def longestConsecutive(self, nums):
        nums.sort()
        longest = 1
        lastSmaller = float("-inf")
        cnt = 1

        for i in range(len(nums)):
            if (nums[i] - 1) == lastSmaller:
                cnt += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                cnt = 1
                lastSmaller = nums[i]
            longest = max(longest, cnt)
        return longest

    def longestConsecutiveOptimal(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        longest = 1
        st = set()

        for num in nums:
            st.add(num)

        for item in st:
            if item - 1 not in st:
                cnt = 1
                x = item

                while x + 1 in st:
                    x = x + 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest

    # Longest subarray with sum K

    # Given an array nums of size n and an integer k, find the length of the longest sub-array that sums up to k. If no such sub-array exists, return 0.
    # Example 1
    # Input: nums = [10, 5, 2, 7, 1, 9],  k=15
    # Output: 4
    # Explanation: The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4.
    # This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

    def longestSubarray(self, nums, k):
        n = len(nums)
        longest = 0

        for i in range(n):

            sum = 0
            for j in range(i, n):

                sum += nums[j]

                if sum == k:
                    cnt = j - i + 1
                    longest = max(cnt, longest)

        return longest

    # Count subarrays with given sum

    # Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
    # Example 1
    # Input: nums = [1, 1, 1], k = 2
    # Output: 2
    # Explanation: In the given array [1, 1, 1], there are two subarrays that sum up to 2: [1, 1] and [1, 1]. Hence, the output is 2.

    def countSubarraySumOptimal(self, nums, k):
        n = len(nums)  
        prefix_sum_map = {0:1}
        current_prefix_sum = 0
        cnt = 0

        for i in range(n):

            current_prefix_sum += nums[i]
            sum_to_remove = current_prefix_sum - k

            cnt += prefix_sum_map.get(sum_to_remove, 0) 
            prefix_sum_map[current_prefix_sum] = prefix_sum_map.get(current_prefix_sum, 0)+1

        return cnt

    def countSubarraySum(self, nums, k):
        n = len(nums)  
        cnt = 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                # calculate the prefix sum till index i
                sum += nums[i]

                # if the sum equals k, update maxLen
                if sum == k:
                    cnt += 1
                    sum = 0

        return cnt
    # Count subarrays with given xor K

    # Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.
    # Example 1
    # Input : nums = [4, 2, 2, 6, 4], k = 6

    # Output : 4

    # Explanation : The subarrays having XOR of their elements as 6 are [4, 2],  [4, 2, 2, 6, 4], [2, 2, 6], and [6]

    def subarraysWithXorKBetter(self, nums, k):
        n = len(nums)

        cnt = 0

        for i in range(n):
            xorr = 0
            for j in range(i, n):

                xorr ^= nums[j]

                if xorr == k:
                    cnt += 1
        return cnt
    
    


if __name__ == "__main__": 
    arr = list(map(int, input().split()))
    sol = Solution()

    res = sol.longestConsecutive(arr)
    print(res)
