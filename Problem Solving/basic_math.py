import math


class Solution:
    # Function to count all digits in n
    def countDigit(self, n):
        # Edge case
        if n == 0:
            return 1

        # Set counter to 0
        cnt = 0

        # Iterate until n is greater than zero
        while n > 0:
            # Extract last digit
            lastDigit = n % 10

            # Increment count of digits
            cnt = cnt + 1
            n = n // 10

        return cnt

    def reverseNumber(self, n):
        
        rev = 0
        
        while n > 0:
            last = n%10
            
            rev = rev * 10 + last
            
            n = n//10
            
        return rev    
    
    
    def largestDigit(self, n):
        large = 0
        
        while n > 0:
            last = n%10
            
            if last > large:
                large = last 
            
            n = n//10
            
        return large    
        
    
    def isPalindrome(self, n): 
        
        if n == self.reverseNumber(n):
            return True
        else:
            return False
    
    
    def factorial(self, n):
        if n <= 1:
            return 1
        fact = 1
        while n > 0:
            fact = fact * n
            n -= 1
        return fact 
    
    def isArmstrong(self, n):
        cnt = 0
        if n == 0:
            cnt = 1
        cnt =  int(math.log10(n)) + 1
        
        sum = 0
        copy = n
        while n > 0:
            last = n%10
            sum = sum + pow(last, cnt)
            n = n//10
        
        if sum == copy:
            return True
        return False
         
    def isPerfect(self, n): 
        sum = 0
        for i in range(1,n):
            
            if n%i == 0:
                sum += i
        
        if sum == n:
            return True
        return False    
    
    def isPrime(self, n):
        for i in range(2,n):
            
            if n%i == 0:
                return False
        
        return True 
    
    
    def primeUptoN(self, n):
        cnt = 0

        for i in range(2, n+1):
            if self.isPrime(i):
                cnt += 1
        return cnt
    
    def GCD(self, n1, n2):
        gcd = 1
        
        limit = n1
        if n1 > n2:
            limit = n2
        for i in range(2, limit+1):
            if n1%i == 0 and n2%i == 0:
                gcd = i
                
        return gcd    
    
    
    def LCM(self, n1, n2): 
        lcm = n1*n2
        num =  max(n1, n2)
        for i in range(1,num+1):
            
            mul = num*i
            if mul%n1 == 0 and mul%n2 == 0:
                lcm = mul
                break
        return lcm    
            
    def divisors(self, n):
        divs = []
        for i in range(1, n+1):
            if n % i == 0:
                divs.append(i)
        return divs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def main(self):
       # N = int(input())
        N1 = int(input())
        N2 = int(input())

        # Create an instance of the Solution class
        # Creating an instance of Solution class
        sol = Solution()

        # Function call to get count of digits in n
        ans = sol.LCM(N1, N2)
        print(f"The ans is: {ans}")

if __name__ == "__main__":
    Solution().main()




