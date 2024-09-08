import array


class Solution:
    # Function to get the highest
    # occurring element in array nums
    def mostFrequentElement(self, nums):

        # Variable to store the size of array
        n = len(nums)

        # Variable to store maximum frequency
        maxFreq = 0

        # Variable to store element
        # with maximum frequency
        maxEle = 0

        # Visited array
        visited = [False] * n

        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue

            # Variable to store frequency
            # of current element
            freq = 0

            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True

            # Update variables if new element having
            # highest frequency is found
            if freq > maxFreq:
                maxFreq = freq
                maxEle = nums[i]
            elif freq == maxFreq:
                maxEle = min(maxEle, nums[i])

        # Return the result
        return maxEle

    def mostFrequentElementOptimized(self, nums):
        n = len(nums)

        maxElement = -1

        for i in range(n):
            if nums[i] > maxElement:
                maxElement = nums[i]

        hash = [0] * (maxElement + 1)

        for i in range(n):
            hash[nums[i]] += 1

        maxcnt = 0
        ele = -1

        for i in range(maxElement + 1):
            if hash[i] > maxcnt:
                maxcnt = hash[i]
                ele = i
        return ele

    def secondMostFrequentElementOptimized(self, nums):
        n = len(nums)

        if n == 0:
            return -1  # Handle the edge case of an empty list

        # Find the maximum element in the array
        maxElement = max(nums)

        # Initialize the hash array with size `maxElement + 1`
        hash = [0] * (maxElement + 1)

        # Count the frequency of each element in the nums array
        for i in range(n):
            hash[nums[i]] += 1

        # Variables to track the most frequent and second most frequent elements
        maxcnt = 0
        second_maxcnt = 0
        ele = -1
        second_ele = -1

        for i in range(maxElement + 1):
            if hash[i] > maxcnt:
                # Update second most frequent before updating the most frequent
                second_maxcnt = maxcnt
                second_ele = ele
                maxcnt = hash[i]
                ele = i
            elif hash[i] == maxcnt:
                ele = min(ele, i)
            elif hash[i] > second_maxcnt:
                second_maxcnt = hash[i]
                second_ele = i
            elif hash[i] == second_maxcnt:
                second_ele = min(second_ele, i)

        # If second most frequent element is not found, return -1

        return second_ele

    def secondMostFrequentElement(self, nums):

        # Variable to store the size of array
        n = len(nums)

        # Variable to store maximum frequency
        maxFreq = secondMaxFreq = 0

        # Variable to store element
        # with maximum frequency
        maxEle = secondMaxEle = -1

        # Visited array
        visited = [False] * n

        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue

            # Variable to store frequency
            # of current element
            freq = 0

            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True

            # Update variables if new element having
            # highest frequency is found
            if freq > maxFreq:
                secondMaxFreq = maxFreq
                secondMaxEle = maxEle
                maxFreq = freq
                maxEle = nums[i]
            elif freq == maxFreq:
                maxEle = min(maxEle, nums[i])
            elif freq > secondMaxFreq:
                secondMaxFreq = freq
                secondMaxEle = nums[i]
            elif freq == secondMaxFreq:
                secondMaxEle = min(secondMaxEle, nums[i])
        # Return the result
        return secondMaxEle

    def sumHighestAndLowestFrequency(self, nums):
        n = len(nums)

        maxFreq = 0
        minFreq = n
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue

            freq = 0
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True

            maxFreq = max(maxFreq, freq)
            minFreq = min(minFreq, freq)
        return maxFreq + minFreq

    def sumHighestAndLowestFrequencyOptimized(self, nums):
        n = len(nums)

        maxElement = max(nums)

        hash = [0] * (maxElement + 1)

        for i in range(n):
            hash[nums[i]] += 1

        maxFreq = 0
        minFreq = n

        for i in range(maxElement + 1):
            if hash[i] > 0:
                maxFreq = max(hash[i], maxFreq)
                minFreq = min(minFreq, hash[i])
        return maxFreq + minFreq


if __name__ == "__main__":
    input_str = input()
    int_list = [int(x) for x in input_str.split()]
    # Creating an instance of Solution class
    sol = Solution()

    # Function call to get the
    # highest occurring element in array nums
    ans = sol.mostFrequentElement(int_list)

    print("The highest occurring element in the array is:", ans)
