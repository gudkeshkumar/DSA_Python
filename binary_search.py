import math


class Solution:
    # Search in rotated sorted array-I

    # Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

    # Example 1
    # Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0
    # Output: 4
    # Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

    def search(self, nums, k):
        n = len(nums)

        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            val = nums[mid]

            if val == k:
                return mid

            if val <= nums[high]:
                if val <= k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                if nums[low] <= k <= val:
                    high = mid - 1
                else:
                    low = mid + 1

        return ans

# Koko eating bananas

# A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. An integer h represents the total time in hours to eat all the bananas.

# Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.

# Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.
# Example 1
# Input: n = 4, nums = [7, 15, 6, 3], h = 8
# Output: 5
# Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.

    def minimumRateToEatBananas(self, nums, h):
     

        low = 1
        high = max(nums)
        ans = -1

        while low <= high:
            mid = (low + high)//2
            sum_val = self.sumByD(nums, mid)
            if sum_val <= h:
                high = mid -1
            else:
                low = mid+1
        return low


    def sumByD(self, nums, div):
        sum_val = 0

        for num in nums:
            sum_val += math.ceil(num/div)
        return sum_val


# Find the smallest divisor

# Given an array of integers nums and an integer limit as the threshold value, find the smallest positive integer divisor such that upon dividing all the elements of the array by this divisor, the sum of the division results is less than or equal to the threshold value.
# Each result of the division is rounded up to the nearest integer greater than or equal to that element.
# Example 1
# Input: nums = [1, 2, 3, 4, 5], limit = 8
# Output: 3
# Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor.
# The sum is 9(1 + 1 + 2 + 2 + 3) if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.


    def smallestDivisor(self, nums, limit):

        n = len(nums)
        if n > limit:
             return -1

        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2
            sum_val = self.sumByD(nums, mid)

            if sum_val <= limit:
                high = mid - 1
            else:
                low = mid + 1
        return low


# Minimum days to make M bouquets
# Example 1
# Input: n = 8, nums = [7, 7, 7, 7, 13, 11, 12, 7], m = 2, k = 3
# Output: 12
# Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.
# Example 2
# Input: n = 5, nums = [1, 10, 3, 10, 2], m = 3, k = 2
# Output: -1
# Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.

    def roseGarden(self, n, nums, k, m):

        if k*m > n:
            return -1
        low = min(nums)
        high = max (nums)

        while low <= high:
            mid = (low + high) // 2

            if self.possible(mid, nums, k, m) == True:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def possible(self, day, nums, k , m):
        n = len(nums)

        cnt = 0
        cob = 0

        for i in range(n):
            if nums[i] <= day:
                cnt += 1
            else:
                cob += (cnt//k)
                cnt = 0
        cob += (cnt//k)

        return cob >= m
     


if __name__ == "__main__":
    input_str = input()
    int_list = [int(x) for x in input_str.split()]
    # Creating an instance of Solution class
    sol = Solution()

    # Function call to get the
    # highest occurring element in array nums
    ans = sol.mostFrequentElement(int_list)

    print("The highest occurring element in the array is:", ans)
