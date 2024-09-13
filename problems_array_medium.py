from typing import List
class Solution:
    
# Leaders in an Array
# Given an integer array nums, return a list of all the leaders in the array.

# A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.
# Example 1
# Input: nums = [1, 2, 5, 3, 1, 2]
# Output: [5, 3, 2]
# Explanation: 2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]


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
    
# Print the matrix in spiral manner
# Given an M * N matrix, print the elements in a clockwise spiral manner. Return an array with the elements in the order of their appearance when printed in a spiral manner.


# Example 1
# Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]

# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Explanation: The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5
    
    def spiralOrder(self, matrix):
        ans = []
        n = len(matrix) #rows
        m = len(matrix[0]) #columns

        # variable for traversal
        top = left = 0
        bottom = n-1
        right = m-1
        
        while left <= right and top <= bottom:
            # left -> right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            #top -> bottom

            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            # right -> left
            if top <= bottom:
                for i in range(right, left -1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            #bottom -> top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
    
# Rearrange array elements by sign
# 100 points


# 41

# Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:



# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Example 1
# Input : nums = [2, 4, 5, -1, -3, -4]

# Output : [2, -1, 4, -3, 5, -4]

# Explanation: The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions
    def rearrangeArray(self, nums):
        ans = [0]*len(nums)
        pos = 0
        neg = 1

        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2
        return ans
    
# Pascal's Triangle

# Given an integer numRows return the first numRows rows of Pascal's triangle.

# In Pascal's triangle:

# The first row has one element with a value of 1.
# Each row has one more element in it than its previous row.
# The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.

    def pascalTriangle(self, numRows):
        ans = self.generate(numRows)
        print(ans)
    
    def nCr(self, n: int, r: int) -> int:
        """
        Choosing the smaller value
        of r to optimize computation
        """
        if r > n - r:
            r = n - r
        
        res = 1
        """
        Calculate nCr using iterative
        method to avoid overflow
        """
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        
        return int(res)

    """ Function to print Pascal's
    Triangle row for given n """
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Initialize the triangle list with numRows lists
        """
        triangle = []
        
        """
        Fill the triangle with Pascal's Triangle values
        """
        for i in range(numRows):
            """
            Create a new row list and
            resize it to i + 1 elements
            """
            row = []
            
            for j in range(i + 1):
                # Compute and store value at position (i, j)
                row.append(self.nCr(i, j))
            
            triangle.append(row)
        
        # Return completed Pascal's Triangle
        return triangle
    
    
# Rotate matrix by 90 degrees

    def rotateMatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(i+1, m):
                    temp = matrix[j][i]
                    matrix[j][i] = matrix[i][j]
                    matrix[i][j] = temp
        for i in range(n):
            matrix[i].reverse()
        return matrix
    
    def twoSum(self, nums, target):
        ans = [-1, -1]
        map = {}
        for i in range(len(nums)):
            cmp = target - nums[i]
            if cmp in map:
                return[map[cmp], i]
            map[nums[i]] = i
        
        return ans
    
# 3 Sum
# Given an integer array nums.Return all triplets such that:

# i != j, i != k, and j != k
# nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. The output and the triplets can be returned in any order.
# Input: nums = [2, -2, 0, 3, -3, 5]

# Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]

# Explanation: nums[1] + nums[2] + nums[0] = 0

# nums[4] + nums[1] + nums[5] = 0
# nums[4] + nums[2] + nums[3] = 0

    def threeSum(self, nums):
       # List to store the triplets that sum up to target
        ans = []
        
        n = len(nums)
        
        # Sort the input array nums
        nums.sort()
        
        # Iterate through the array to find triplets
        for i in range(n):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers approach
            j = i + 1
            k = n - 1
            
            while j < k:
                sum_val = nums[i] + nums[j] + nums[k]
                
                if sum_val < 0:
                    j += 1
                elif sum_val > 0:
                    k -= 1
                else:
                    # Found a triplet that sums up to target
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    
                    # Skip duplicates
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return ans

# 4 Sum

# Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# ·      a, b, c, d are all distinct valid indices of nums.
# ·      nums[a] + nums[b] + nums[c] + nums[d] == target.
# Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets. The output and the quadruplets can be returned in any order.
# Example 1
# Input: nums = [1, -2, 3, 5, 7, 9], target = 7

# Output: [[-2, 1, 3, 5]]

# Explanation: nums[1] + nums[0] + nums[2] + nums[3] = 7

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        # Sort the input array nums
        nums.sort()
        
        # Iterate through the array to find quadruplets
        for i in range(n):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two pointers approach
                k = j + 1
                l = n - 1
                
                while k < l:
                    sum_val = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if sum_val == target:
                        # Found a quadruplet that sums up to target
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        
                        # Skip duplicates for k and l
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif sum_val < target:
                        k += 1
                    else:
                        l -= 1
        
        return ans
# Sort an array of 0's 1's and 2's

# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
# Example 1
# Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

    def sortZeroOneTwo(self, nums):
        n = len(nums)
        low, mid, high = 0, 0, n-1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Kadane's Algorithm

# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.


# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1
# Input: nums = [2, 3, 5, -2, 7, -4]
# Output: 15
# Explanation: The subarray from index 0 to index 4 has the largest sum = 15

    def maxSubArray(self, nums):
        maxi = float('-inf')
        n = len(nums)
        sumv = 0

        for num in nums:
            sumv += num
            maxi = max(maxi, sumv)
            if sumv < 0:
                sumv = 0

        return maxi


# Main function
if __name__ == "__main__":
    # Accept input for the list of numbers and target
    #nums = list(map(int, input().split()))

    # Create an instance of the Solution class
    #sol = Solution()

    # Call the linearSearch method and store the result
    #result = sol.leaders(nums)

    #print(result)
    # Accept input for the matrix dimensions
    rows = int(input()) # "Enter the number of rows: "
    # cols = int(input()) # "Enter the number of columns: "

    # # Initialize an empty matrix
    # mat = []

    # # Accept input for the matrix row by row
    # print("Enter the matrix row by row (space-separated values):")
    # for i in range(rows):
    #     row = list(map(int, input().split()))  # Read a row of integers
    #     if len(row) != cols:
    #         print(f"Error: You must enter exactly {cols} numbers per row.")
    #         exit()
    #     mat.append(row)

    # Create an instance of the Solution class
    finder = Solution()

    # Get spiral order using the class method
    ans = finder.pascalTriangle(rows)

    # Print the result
    print(ans)