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

    # Aggressive Cows

    # Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. Find the maximum possible minimum distance.
    # Example 1
    # Input: n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9]
    # Output: 3
    # Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions [0, 3, 7, 10]. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

    def aggressiveCows(self, nums, k):
        n = len(nums)
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]

        while low <= high:
            mid = (low + high)//2

            if self.canWePlace(nums, mid, k) == True:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def canWePlace(self, nums, mid, k):
        last = nums[0]
        cnt = 1

        for i in range(1, n):
            if nums[i] - last >= mid:
                cnt += 1 
                last = nums[i]
            if cnt >= k:
                return True
        return False

    # Book Allocation Problem

    # Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.

    # Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.
    # Example 1
    # Input: nums = [12, 34, 67, 90], m=2
    # Output: 113
    # Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

    def findPages(self, nums, m):
        if m > len(nums):
            return -1
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            cnt = self.countStudents(nums, mid)
            if cnt > m:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def countStudents(self, nums, limit):
        cnt = 1
        pages = 0

        for i in range(len(nums)):
            if nums[i] + pages <= limit:
                pages += nums[i]
            else:
                cnt += 1
                pages = nums[i]
        return cnt

    # Find peak element

    # Given an array arr of integers. A peak element is defined as an element greater than both of its neighbors. Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.
    # Example 1
    # Input : arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    # Output: 7
    # Explanation: In this example, there is only 1 peak that is at index 7.

    def findPeakElement(self, arr):
        n = len(arr)

        if (n == 0) or (arr[0] > arr[1]):
            return 0
        if arr[n - 1] > arr[n - 2]:
            return n - 1

        low = 1
        high = n - 2

        while low <= high:
            mid = (low + high) // 2

            if (arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
                return mid
            if arr[mid] < arr[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
# Kth element of 2 sorted arrays
# Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.
# Example 1
# Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
# Output: 6
# Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

    def kthElement(self, arr1, arr2, k):
        n1, n2 = len(arr1), len(arr2)

        if n1 > n2:
            return self.kthElement(arr2, arr1, k)
        
        n = n1+n2

        left = k

        low = max(0, k - n2)
        high = min(k, n1)

        while low <= high:

            mid1 = (low+high) >> 1
            mid2 = left - mid1

            l1 = arr1[mid1 -1 ] if mid1 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < n1 else float('inf')
            l2 = arr2[mid2 -1 ] if mid2 > 0 else float('-inf')
            r2 = arr2[mid2] if mid2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:

                return max(l1,l2)

            elif l1 > r2:
                high = mid1 -1
            else:
                low = mid1+ 1
        return -1

# Median of 2 sorted arrays
# Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays.
#
# The median is defined as the middle value of a sorted list of numbers. In case the length of the list is even, the median is the average of the two middle elements.
# Example 1
# Input: arr1 = [2, 4, 6], arr2 = [1, 3, 5]
# Output: 3.5
# Explanation: The array after merging arr1 and arr2 will be [ 1, 2, 3, 4, 5, 6 ]. As the length of the merged list is even, the median is the average of the two middle elements. Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.
    def median(self, arr1, arr2):
        n1, n2 = len(arr1), len(arr2)

        if n1 > n2:
            return self.median(arr2, arr1)
        
        n = n1+n2

        left = (n+1) >> 1

        low = 0
        high = n1

        while low <= high:

            mid1 = (low+high) >> 1
            mid2 = left - mid1

            l1 = arr1[mid1 -1 ] if mid1 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < n1 else float('inf')
            l2 = arr2[mid2 -1 ] if mid2 > 0 else float('-inf')
            r2 = arr2[mid2] if mid2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:

                if n%2 == 1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 -1
            else:
                low = mid1+ 1
        return -1




if __name__ == "__main__":
    input_str = input()
    int_list = [int(x) for x in input_str.split()]
    # Creating an instance of Solution class
    sol = Solution()

    # Function call to get the
    # highest occurring element in array nums
    ans = sol.mostFrequentElement(int_list)

    print("The highest occurring element in the array is:", ans)
