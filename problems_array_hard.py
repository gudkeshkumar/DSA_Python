from collections import defaultdict
from typing import List

class Solution:

    # Majority Element-I

    # Given an integer array nums of size n, return the majority element of the array.
    # The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

    # Example 1
    # Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
    # Output: 7
    # Explanation: The number 7 appears 5 times in the 9 sized array

    def majorityElement(self, nums):
        n = len(nums)
        fmap = {}
        for i in range(n):
            if nums[i] in fmap:
                fmap[nums[i]] += 1
            else:
                fmap[nums[i]] = 1
        for ele, fre in fmap.items():

            if fre > n // 2:
                return ele
        return -1

    def majorityElementOptimal(self, nums):
        n = len(nums)
        el = 0
        ct = 0

        for num in nums:
            if ct == 0:
                el = num
                ct = 1
            elif num == el:
                ct += 1
            else:
                ct -= 1

        cnt = nums.count(el)
        if cnt > (n // 2):
            return el
        return -1

    # Majority Element-II

    # Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.

    # Example 1
    # Input: nums = [1, 2, 1, 1, 3, 2]

    # Output: [1]
    # Explanation: Here, n / 3 = 6 / 3 = 2.
    # Therefore the elements appearing 3 or more times is : [1]

    def majorityElementTwo(self, nums):
        n = len(nums)
        ans = []
        mpp = defaultdict(int)
        moc = (n // 3) + 1
        for num in nums:
            mpp[num] += 1
            if mpp[num] == moc:
                ans.append(num)
            if len(ans) == 2:
                break
        return ans

    def majorityElementTwoOptimal(self, nums):
        n = len(nums)
        ans = []
        moc = (n//3)
        c1, c2 = 0,0
        el1 , el2 = float('-inf'), float('-inf')
        for num in nums:
            if c1 == 0 and num != el2:
                c1 = 1
                el1 = num
            elif c2 == 0 and num != el1:
                c2= 1
                el2 = num
            elif num == el1:
                c1 += 1
            elif num == el2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = nums.count(el1)
        c2 = nums.count(el2)

        if c1 > moc:
            ans.append(el1)
        if c2 > moc:
            ans.append(el2)

        return ans

    # Find the repeating and missing number

    # Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
    # Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.

    # Example 1
    # Input: nums = [3, 5, 4, 1, 1]
    # Output: [1, 2]
    # Explanation: 1 appears two times in the array and 2 is missing from nums

    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        arr =[0]*(n+1)
        duplicate = 0
        missing = 0
        for i in range(n):
            arr[nums[i]] += 1
        for i in range(0, n+1):
            if arr[i] == 0:
                missing = i
            if arr[i] == 2:
                duplicate = i
        return [duplicate, missing]

    def findMissingRepeatingNumbersOptimal1(self, nums):
        n = len(nums)
        sn = (n*(n+1))//2
        s2n = (n*(n+1)*(2*n+1))//6
        sa = 0
        s2a = 0

        for num in nums:
            sa += num
            s2a += num*num

        val1 = sa - sn
        val2 = s2a - s2n
        val2 = val2//val1

        x = (val1+val2)//2
        y = x-val1
        return [x, y]

    # Count Inversions

    # Given an integer array nums. Return the number of inversions in the array.

    # Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
    # It indicates how close an array is to being sorted.
    # A sorted array has an inversion count of 0.
    # An array sorted in descending order has maximum inversion.
    # Example 1
    # Input: nums = [2, 3, 7, 1, 3, 5]
    # Output: 5
    # Explanation: The responsible indexes are:
    # nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
    # nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
    # nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
    # nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
    # nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5

    def numberOfInversions(self, nums):
        # Size of the array
        n = len(nums)

        # Count the number of pairs
        return self.mergeSort(nums, 0, n - 1)

    def mergeSort(self, arr, low, high):
        cnt = 0
        if low < high:
            mid = low + (high - low) // 2
            cnt += self.mergeSort(arr, low, mid)
            cnt += self.mergeSort(arr, mid + 1, high)
            cnt += self.merge(arr, low, mid, high)
        return cnt

    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        cnt = 0
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:  # right is smaller
                temp.append(arr[right])
                cnt += mid - left + 1
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        return cnt

    # Maximum Product Subarray in an Array

    # Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.

    # A subarray is a contiguous non-empty sequence of elements within an array.
    # Example 1
    # Input: nums = [4, 5, 3, 7, 1, 2]
    # Output: 840
    # Explanation: The largest product is given by the whole array itself
    # Example 2
    # Input: nums = [-5, 0, -2]
    # Output: 0
    # Explanation: The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, 2].

    def maxProduct(self, nums):
        ans = float("-inf")
        pre = 1
        suf = 1
        n = len(nums)

        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1

            pre *= nums[i]
            suf *= nums[n - i - 1]
            ans = max(ans, max(suf, pre))
        return ans

# Merge two sorted arrays without extra space

# Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.

# Merge both the arrays into a single array sorted in non-decreasing order.
# The final sorted array should be stored inside the array nums1 and it should be done in-place.
# nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
# nums2 has a length of n.
# Example 1
# Input: nums1 = [-5, -2, 4, 5], nums2 = [-3, 1, 8]
# Output: [-5, -3, -2, 1, 4, 5, 8]
# Explanation: The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1 and [-3, 1, 8] are from nums2

    def merge(self, nums1, m, nums2, n):
        left = m-1
        right = 0

        while left >= 0 and right < n:
            if nums1[left] > nums2[right]:
                temp = nums1[left]
                nums1[left] = nums2[right]
                nums2[right] = temp
                left -= 1
                right += 1
            else:
                break
        nums1[:m] = sorted(nums1[:m])
        nums2.sort()

        for i in range(m, m+n):
            nums1[i] = nums2[i-m]

# Main function
if __name__ == "__main__": 
    arr = list(map(int, input().split()))
    sol = Solution()

    res = sol.majorityElement(arr)
    print(res)
