class Solution:
    def NnumbersSum(self, N):
        # Base case: if N is 0, return 0
        if N == 0:
            return 0
        # Recursive case: add N to the sum of N-1
        return N + self.NnumbersSum(N - 1)

    def factorial(self, n):
        # Your code goes here
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)

    def addDigits(self, num):
        # Base case: if the number is a single digit, return it
        if num < 10:
            return num

        # Recursive case: sum the digits and continue
        return self.addDigits(sum(int(digit) for digit in str(num)))

    def reverseString(self,s):
        # your code goes here
        if len(s) == 1:
            return s
        def reverse(s, left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            reverse(s, left+1, right-1)

        reverse(s, 0, len(s) -1)
        return s

    def palindromeCheck(self, s: str) -> bool:
        return self.isPalindrome(s, 0, len(s) - 1)

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.isPalindrome(s, left + 1, right - 1)

    def arraySum(self, nums):
        # Start from index 0
        return self.sum(nums, 0)

    def sum(self, nums, left):
        # Base case: out of bounds
        if left >= len(nums):
            return 0
        # Add current element and recurse
        return nums[left] + self.sum(nums, left + 1)

    def checkPrime(self, num):
        if num <= 1:
            return False  # 0 and 1 are not prime numbers
        return self.prime(num, 2)  # Call the helper function to check for primality

    def prime(self, num, x):
        # Base case: x > sqrt(num), so the number is prime
        if x > num**0.5:
            return True
        if num % x == 0:
            # Found a divisor, so the number is not prime
            return False
        # Recursive call with the next divisor
        return self.prime(num, x + 1)

    def fib(self, n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)

    def isSorted(self, nums):
        # Ensure nums is a list to use len() function
        nums = list(nums)
        # An array with 0 or 1 element is always considered sorted
        if len(nums) <= 1:
            return True
        # Check if the array is sorted starting from index 0 to 1
        return self.sort(nums, 0, 1)

    def sort(self, nums, left, right):
        # If we reach the end of the array
        # it means the array is sorted
        if right >= len(nums):
            return True
        # If we find a pair where the left element is greater than the right
        # the array is not sorted
        if nums[left] > nums[right]:
            return False
        # Move to the next pair of elements
        return self.sort(nums, left + 1, right + 1)


if __name__ == "__main__":
    solution = Solution()
    N = int(input())  # Example input
    print(f"Sum of first {N} numbers is {solution.NnumbersSum(N)}")
