class Solution:
    
    def pattern1(self, n):

        for i in range(n):
            for j in range(n):
                print("*", end = '')
            print()
    
    # Function to print pattern2
    def pattern2(self, n):
        
        # Outer loop will run for rows.
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(i+1):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

   
   
    def pattern3(self, n):

        for i in range(1,n+1):
            for j in range(1, i+1):
                print(j, end = '')
            print()
   
   
    def pattern4(self, n):

        for i in range(1,n+1):
            for j in range(1, i+1):
                print(i, end = '')
            print()   
   
   
    def pattern5(self, n):

        for i in range(1,n+1):
            for j in range(n-i+1):
                print("*", end = '')
            print()    
   
   
    def pattern6(self, n):

        for i in range(1,n+1):
            for j in range(1, n-i+2):
                print(j, end = '')
            print() 
                
   
    def pattern7(self, n):

        for i in range(1,n+1):
            for j in range(1, n-i+1):
                print(" ", end = '')
                
            for j in range(1, 2*i):
                print("*", end = '')
            
            for j in range(1, n-i+1):
                print(" ", end = '')
            print()    
   
   
    def pattern8(self, n):

        for i in range(n):
            for j in range(i):
                print(" ", end = '')
                
            for j in range(0, (2*n - 1) - 2*i):
                print("*", end = '')
            
            for j in range(i):
                print(" ", end = '')
            print()  
   
   
   
    def pattern9(self, n):
        self.pattern7(n)
        self.pattern8(n)

            
            
    def pattern10(self, n):

        for i in range(1, 2*n):
            
            if i <= n:
                for j in range(i):
                    print("*", end = '')
            else:
                for j in range(2*n - i):
                    print("*", end = '')
            print()          
               
    def pattern11(self, n):

        for i in range(n):
            start = 1
            if i%2:
             start = 0
            for j in range(i+1):
                print(start, end = '')
                start = 1 - start
            print()
    
    
    def pattern12(self, n):
        for i in range(1, n + 1):
            
            for j in range(1, i+1):
                print(j, end = " ")
                
            for j in range(2*n - 2*i):
                print(" ", end= " ")
                
            for j in range(i, 0, -1):
                print(j, end = " ")
        
            print() 
   
    def pattern13(self, n):
        start = 1
        for i in range(1, n+1):
           
            for j in range(i):
                print(start, end = '')
                start += 1
            print()
            
            
    def pattern14(self, n):
        for i in range(n):
            for j in range(ord('A'), ord('A') + i + 1):
                print(chr(j), end = '')
            print() 
            
            
    def pattern15(self, n):
        for i in range(n):
            for j in range(ord('A'), ord('A') + n - i ):
                print(chr(j), end = '')
            print()   
    
    def pattern16(self, n):
        start = ord('A') 
        for i in range(n):
            for j in range( i+1 ):
                print(chr(start+i), end = '')
            print() 
    
    def pattern17(self, n):
        for i in range(1, n+1):
            ch = ord('A')
            for j in range(n - i):
                print(" ", end= '')
                
            for j in range(2*i - 1):
                if j <= (2*i - 1)//2:
                    ch+=1
                    print(chr(ch-1), end= '')
                    
                else:
                    ch -= 1
                    print(chr(ch-1), end= '')
                    
                    
            for j in range(n - i):
                print(" ", end= '')
            print()
    
    
    def pattern22(self, n):
        # Outer loop for the rows
        for i in range(2 * n - 1):
            # Inner loop for the columns
            for j in range(2 * n - 1):
                
                """ Initialising the top, down, left
                and right indices of a cell"""
                top = i
                bottom = j
                right = (2 * n - 2) - j
                left = (2 * n - 2) - i
                
                """ Minimum of 4 directions and then we 
                subtract from n because previously we 
                would get a pattern whose border has 0's, 
                but we want with border n's and then
                decreasing inside."""
                print((n - min(min(top, bottom), min(left, right))), end=" ")
                
            # Move to the next row
            print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def main(self):
        N = int(input())

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern22(N)

if __name__ == "__main__":
    Solution().main()


