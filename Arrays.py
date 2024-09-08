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
        return maxFreq+minFreq
        
                    
                    
                    
                    
if __name__ == "__main__":
    input_str = input()
    int_list = [int(x) for x in input_str.split()]
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to get the
    # highest occurring element in array nums
    ans = sol.mostFrequentElement(int_list)
    
    print("The highest occurring element in the array is:", ans)