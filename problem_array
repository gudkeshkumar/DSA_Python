from typing import List

class Solution:
    # Linear Search Function
    def linearSearch(self, nums: List[int], target: int) -> int:
        # Traverse the entire array
        for i in range(len(nums)):

            # Check if current element is target
            if nums[i] == target:

                # Return index if target found
                return i

        # If target not found
        return -1

    def secondLargestElement(self, nums):
        l1 = float("-inf")
        l2 = float("-inf")
        if len(nums) < 2:
            return -1

        for num in nums:
            if num > l1:
                l2 = l1  # Update second largest to previous largest
                l1 = num  # Update largest
            elif num > l2 and num != l1:
                l2 = num  # Update second largest if it's not equal to the largest

        if l2 == float("-inf"):
            return -1

        return l2

    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        maxcnt = 0

        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            maxcnt = max(maxcnt, cnt)

        return maxcnt

    def rotateArrayByOne(self, nums):
        n = len(nums)
        tmp = nums[0]

        for i in range(1, n):
            nums[i - 1] = nums[i]
        nums[n - 1] = tmp
        return nums

    def rotateArray(self, nums, k):
        n = len(nums)
        if k > n:
            k = k % n
        self.reverseArray(nums, 0, k - 1)
        self.reverseArray(nums, k, n - 1)
        self.reverseArray(nums, 0, n - 1)

    def reverseArray(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1  

    def rotateArray2(self, nums, k):
        n = len(nums)
        if k > n:
            k = k % n
        temp = [0] * k

        for i in range(k):
            temp[i] = nums[i]

        for i in range(k, n):
            nums[i - k] = nums[i]

        for i in range(n - k, n):
            nums[i] = temp[i - (n - k)]
            
    
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, n):
            nums[i] = 0
        return nums

    def moveZeroesOptimal(self, nums):
        n = len(nums)
        j = -1 
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return
        for i in range(j+1, n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
    
    def removeDuplicatesBruteForce(self, nums):
        n = len(nums)
        temp = []
        k = 0
        for i in range(n):
            if nums[i] not in temp:
                temp.append(nums[i])
                k = i
        for i in range(k+1):
            nums[i] = temp[i]
        return k
    
    def removeDuplicatesOptimal(self, nums):
        n = len(nums)
        i = 0
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(0, n+1):
            if i not in nums:
                return i
        return -1
    
    def missingNumberBetter(self, nums):
        n = len(nums)
        arr =[0]*(n+1)
        for i in range(0, n):
            arr[nums[i]] = 1
        for i in range(0, n+1):
            if arr[i] == 0:
                return i
        return -1
    
    def missingNumberOptimal(self, nums):
        xor1 = 0
        xor2 = 0
        n = len(nums)
        for i in range(n):
            xor1 ^= i+1
            xor2 ^= nums[i]

        return xor1^xor2
    
    def unionArray(self, nums1, nums2)-> List[int]:
        n, m = len(nums1), len(nums2)
        union = []
        i, j = 0, 0
        
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                if not union or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i +=1
            else:
                if not union or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j +=1

        while i < n:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i +=1
        while j < m:
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j +=1

        return union
    
    def intersectionArray(self, nums1, nums2):
        ans = []  

         # Pointers for nums1 and nums2
        i, j = 0, 0 

        # Traverse both arrays using two pointers approach
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
          # nums1[i] == nums2[j]
            else:  
                ans.append(nums1[i])
                i += 1
                j += 1

        return ans


            
# Main function
if __name__ == "__main__":
    # Accept input for the list of numbers and target
    nums = list(map(int, input().split()))
    target = int(input())

    # Create an instance of the Solution class
    sol = Solution()

    # Call the linearSearch method and store the result
    result = sol.linearSearch(nums, target)

    print(result)
