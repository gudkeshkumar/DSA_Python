class Solution:

    def myPowIterative(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = x * ans
                n = n - 1
            else:
                x = x * x
                n = n / 2
        return ans

    def myPowRec(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        if n%2 == 1:
            return x * self.myPowRec(x, n-1)
        return self.myPow(x*x, n/2)

    # Generate Paranthesis

    # Given an integer n.Generate all possible combinations of well-formed parentheses of length 2 x N.
    # Example 1
    # Input : n = 3
    # Output : [ "((()))" , "(()())" , "(())()" , "()(())" , "()()()" ]

    def generateParenthesis(self, n):
        ans = []
        self._generate(0,0, n, "", ans)
        return ans

    def _generate(self, opcnt: int, clscnt: int, n: int, current: str, ans: list ):
        if open == clscnt == n:
            ans.append(current)
            return
        if opcnt < n:
            self._generate(opcnt+1, clscnt, n, current+')', ans)
        if clscnt < n:
            self._generate(opcnt, clscnt+1, n, current + "(", ans)

    # Power Set
    # Given an array of integers nums of unique elements. Return all possible subsets (power set) of the array.

    # Do not include the duplicates in the answer.
    # Example 1
    # Input : nums = [1, 2, 3]
    # Output : [ [ ] , [1] , [2] , [1, 2] , [3] , [1, 3] , [2, 3] , [1, 2 ,3] ]

    def powerSet(self, nums):
        # your code goes here
        ans = []
        current =[]
        self.generatePowerSet(0, len(nums), nums, current, ans)
        return ans

    def generatePowerSet(self, ind: int, n: int, nums: list, current: list, ans: list):

        if ind == n:
            ans.append(current[:])
            return

        self.generatePowerSet(ind + 1, n, nums, current, ans)

        current.append(nums[ind])
        self.generatePowerSet(ind + 1, n, nums, current, ans)

        # backtrack
        current.pop()

    # Check if there exists a subsequence with sum K

    # Given an array nums and an integer k. Return true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.
    # Example 1
    # Input : nums = [1, 2, 3, 4, 5] , k = 8
    # Output : Yes
    # Explanation : The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

    def checkSubsequenceSum(self, nums, k):
        # your code goes here
        n = len(nums)
        return self.checkSum(0, n, nums, k)

    def checkSum(self, i, n, nums, k):
        if k == 0:
            return True
        if k < 0:
            return False
        if i == n:
            return k==0
        return self.checkSum(i+1, n, nums, k - nums[i]) or self.checkSum(i+1, n, nums, k)

    # Count all subsequences with sum K

    # Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.
    # Example 1
    # Input : nums = [4, 9, 2, 5, 1] , k = 10
    # Output : 2
    # Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].

    def countSubsequenceWithTargetSum(self, nums, k):
        # your code goes here
        n = len(nums)
        return self.countSubsequenceWithSum(0, n, nums, k)

    def countSubsequenceWithSum(self, i, n, nums, k):
        if k == 0:
            return 1
        if k < 0 or i == n:
            return 0

        cn1 = self.countSubsequenceWithSum(i + 1, n, nums, k - nums[i])
        cn2 = self.countSubsequenceWithSum(i + 1, n, nums, k)
        return cn1 + cn2

    # Combination Sum
    # Provided with a goal integer target and an array of unique integer candidates, provide a list of all possible combinations of candidates in which the selected numbers add up to the target. The combinations can be returned in any order.
    # A candidate may be selected from the pool an infinite number of times. There are two distinct combinations if the frequency if at least one of the selected figures differs.

    # The test cases are created so that, for the given input, there are fewer than 150 possible combinations that add up to the target.
    # If there is no possible subsequences then return empty vector.
    # Example 1
    # Input : candidates = [2, 3, 5, 4] , target = 7
    # Output : [ [2, 2, 3] , [3, 4] , [5, 2] ]
    # Explanation :
    # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    # 5 and 2 are candidates, and 5 + 2 = 7.
    # 3 and 4 are candidates, and 3 + 4 = 7.
    # There are total three combinations.

    def combinationSum(self, candidates, target):
        # your code goes here
        ans = []
        current = []
        n = len(candidates) - 1
        self.func(candidates, n, target, current, ans)
        return ans

    def func(self, arr, n, target, current, ans):
        if target == 0:
            ans.append(current[:])
            return
        if target < 0 or n < 0:
            return

        self.func(arr, n - 1, target, current, ans)

        current.append(arr[n])

        self.func(arr, n, target - arr[n], current, ans)

        current.pop()

    # Combination Sum II
    # Given collection of candidate numbers (candidates) and a integer target.Find all unique combinations in candidates where the sum is equal to the target.There can only be one usage of each number in the candidates combination and return the answer in sorted order.

    # e.g : The combination [1, 1, 2] and [1, 2, 1] are not unique.
    # Example 1
    # Input : candidates = [2, 1, 2, 7, 6, 1, 5] , target = 8
    # Output : [ [1, 1, 6] , [1, 2, 5] , [1, 7] , [2, 6] ]
    # Explanation : The combinations sum up to target are
    # 1 + 1 + 6 => 8.
    # 1 + 2 + 5 => 8.
    # 1 + 7 => 8.
    # 2 + 6 => 8.

    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []

        n = len(candidates)

        current = []

        self.c2Func(n, 0, candidates, current, ans, target)

        return ans

    def c2Func(self, n, ind, candidates, current, ans, sum):

        if sum == 0:
            ans.append(current[:])
            return
        if sum < 0 or ind == n:
            return

        current.append(candidates[ind])
        self.c2Func(n, ind + 1, candidates, current, ans, sum - candidates[ind])

        current.pop()

        for i in range(ind + 1, n):
            if candidates[i] != candidates[ind]:
                self.c2Func(n, i, candidates, current, ans, sum)
                break

    # Combination Sum III
    # There is only use of numerals 1 through 9.
    # A single use is made of each number.

    # Return list of every feasible combination that is allowed. The combinations can be returned in any order, but the list cannot have the same combination twice.
    # Example 1
    # Input : k = 3 , n = 7
    # Output : [ [1, 2, 4] ]
    # Explanation :
    # 1 + 2 + 4 = 7
    # There are no other valid combinations.

    def combinationSum3(self, k, n):
        # your code goes here
        ans = []
        cur = []
        self.findCombination(n, 1, cur, ans, k)
        return ans

    def findCombination(self, sum, last, cur, ans, k):
        if sum == 0 and k == len(cur):
            ans.append(cur[:])
            return
        if sum < 0 or k < len(cur):
            return

        for i in range(last, 10):
            if i <= sum:
                cur.append(i)
                self.findCombination(sum - i, i + 1, cur, ans, k)
                cur.pop()
            else:
                break

    # Subsets I
    # Given an array nums of n integers.Return sum of all subsets of the array nums.

    # Output can be printed in any order.
    # Example 1
    # Input : nums = [2, 3]
    # Output : [0, 2, 3, 5]
    # Explanation :
    # When no elements is taken then Sum = 0.
    # When only 2 is taken then Sum = 2.
    # When only 3 is taken then Sum = 3.
    # When element 2 and 3 are taken then sum = 2+3 = 5.

    def subsetSums(self, nums):
        ans = []
        current = []
        self.generateSubsetSum(0, len(nums), nums, current, ans, 0)
        return ans

    def generateSubsetSum(self, ind: int, n: int, nums: list, current: list, ans: list, sum: int):

        if ind == n:
            ans.append(sum)
            return

        self.generateSubsetSum(ind + 1, n, nums, current, ans, sum)

        current.append(nums[ind])
        sum += nums[ind]
        self.generateSubsetSum(ind + 1, n, nums, current, ans, sum)

        # backtrack
        current.pop()
        sum -= nums[ind]

    # Subsets II

    # Given an integer array nums, which can have duplicate entries, provide the power set. Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.
    # Example 1
    # Input : nums = [1, 2, 2]
    # Output : [ [ ] , [1] , [1, 2] , [1, 2, 2] , [2] , [2, 2] ]

    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        current = []
        self.generate(0, len(nums), nums, current, ans)
        return ans

    def generate(self, ind: int, n: int, nums: list, current: list, ans: list):

        if ind == n:
            ans.append(current[:])
            return

        current.append(nums[ind])
        self.generate(ind + 1, n, nums, current, ans)

        current.pop()
        # sum += nums[ind]

        for i in range(ind + 1, n):
            if nums[i] != nums[ind]:
                self.generate(i, n, nums, current, ans)
                return

        self.generate(n, n, nums, current, ans)

    # Letter Combinations of a Phone Number
    # Given a string consisting of digits from 2 to 9 (inclusive). Return all possible letter combinations that the number can represent.

    # Mapping of digits to letters is given in first example.
    # Example 1
    # Input : digits = "34"
    # Output : [ "dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi" ]
    # Explanation : The 3 is mapped with "def" and 4 is mapped with "ghi".
    # So all possible combination by replacing the digits with characters are shown in output.

    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        # your code goes here
        ans = []
        if not digits:
            return ans

        self.helper(digits, ans, 0, "")
        return ans

    def helper(self, digits, ans, index, current):

        if index == len(digits):
            ans.append(current)
            return

        str = self.map[int(digits[index])]

        for char in str:
            self.helper(digits, ans, index + 1, current + char)

    # N Queen

    # The challenge of arranging n queens on a n × n chessboard so that no two queens attack one another is known as the "n-queens puzzle."
    # Return every unique solution to the n-queens puzzle given an integer n. The answer can be returned in any sequence.

    # Every solution has a unique board arrangement for the placement of the n-queens, where 'Q' and '.' stand for a queen and an empty space, respectively.
    # Example 1
    # Input : n = 4
    # Output : [[".Q.." , "...Q" , "Q..." , "..Q."] , ["..Q." , "Q..." , "...Q" , ".Q.."]]
    # Explanation : There are two possible combinations as shown below.

    def solveNQueens(self, n):
        # your code goes here
        ans = []
        board = ["." * n for _ in range(n)]
        self.func(0, ans, board)
        return ans

    def func(self, col, ans, board):
        if col == len(board):
            ans.append(list(board))
            return

        for row in range(len(board)):

            if self.valid(board, row, col):

                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]

                self.func(col + 1, ans, board)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

    def valid(self, board, row, col):

        r = row
        c = col

        # check upper left diagonal
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        r, c = row, col

        # check left
        while c >= 0:
            if board[r][c] == "Q":
                return False
            c -= 1

        r, c = row, col

        while c >= 0 and r < len(board):
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1
        return True

    # Word Search

    # Given a grid of n x m dimension grid of characters board and a string word.The word can be created by assembling the letters of successively surrounding cells, whether they are next to each other vertically or horizontally. It is forbidden to use the same letter cell more than once.
    # Return true if the word exists in the grid otherwise false.
    # Example 1
    # Input : board = [ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ] , word = "ABCCED"
    # Output : true
    # Explanation : The word is coloured in yellow.

    def exist(self, board, word):
        # your code goes here
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.wordSearch(board, i, j, word, 0):
                        return True
        return False

    def wordSearch(self, board, i, j, word, ind):

        if ind == len(word):
            return True

        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or word[ind] != board[i][j]
        ):
            return False

        temp = board[i][j]
        board[i][j] = " "

        ans = (
            self.wordSearch(board, i - 1, j, word, ind + 1)
            or self.wordSearch(board, i + 1, j, word, ind + 1)
            or self.wordSearch(board, i, j - 1, word, ind + 1)
            or self.wordSearch(board, i, j + 1, word, ind + 1)
        )

        board[i][j] = temp
        return ans

    # Rat in a Maze
    # Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1).Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).

    # The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for travelling, whereas value 1 represents that rat can travel through the cell. If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.
    # Example 1
    # Input : n = 4 , grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
    # Output : [ "DDRDRR" , "DRDDRR" ]
    # Explanation : The rat has two different path to reach (3, 3).
    # The first path is (0, 0) => (1, 0) => (2, 0) => (2, 1) => (3, 1) => (3, 2) => (3, 3).
    # The second path is (0,0) => (1,0) => (1,1) => (2,1) => (3,1) => (3,2) => (3,3).

    def findPath(self, grid):
        # your code goes here
        n = len(grid)
        ans = []

        if grid[0][0] == 0 or grid[n-1][n-1] == 0:
            return ans

        self.path(grid, 0, 0, "", n, ans)

        return ans

    def path(self, grid, x, y, dir, n, ans):

        if x == n-1 and y == n-1:
            ans.append(dir)
            return

        if grid[x][y] == 0:
            return

        grid[x][y] = 0

        # Move up
        if x > 0:
            self.path(grid, x-1, y, dir+'U', n, ans)

        # Move Down

        if x < n-1:
            self.path(grid, x+1, y, dir+'D', n, ans)

        if y > 0:
            self.path(grid, x, y-1, dir+'L', n, ans)

        if y < n-1:
            self.path(grid, x, y+1, dir+'R', n, ans)

        grid[x][y] = 1

    # Sudoko Solver
    # Create a program that fills in the blank cells in a Sudoku puzzle to solve it.
    # Every sudoku solution needs to follow to these guidelines:
    # 1) In every row, the numbers 1 through 9 must appear exactly once.
    # 2) In every column, the numbers 1 through 9 must appear exactly once.
    # 3) In each of the grid's nine 3x3 sub-boxes, the numbers 1 through 9 must appear exactly once.

    # Empty cells are indicated by the '.' character.

    def solveSudoku(self, board):
        # your code goes here
        self.solve(board)

    def solve(self, board):
        n = 9

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    for digit in "123456789":
                        if self.isSolution(board, i, j, digit):
                            board[i][j] = digit
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def isSolution(self, board, row, col, digit):

        for i in range(9):
            if board[i][col] == digit or board[row][i] == digit:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == digit:
                    return False
        return True
