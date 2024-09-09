class Solution:
    def reverseString(self, s):
        s_list = list(s)

        left = 0
        right = len(s_list) - 1

        while left < right:
            # Swap characters
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        # Convert the list back to a string and return
        return "".join(s_list)

    def palindromeCheck(self, s):
        left = 0
        right = len(s) - 1

        # Iterate while  start pointer is less than end pointer
        while left < right:
            # If characters  don't match, it's not a palindrome
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def largeOddNum(self, s):
        left = 0
        right = len(s) - 1

        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 != 0:
                right = i
                break

        if right == 0:
            return ""
        for i in range(right + 1):
            if int(s[i]) != 0:
                left = i
                break

        ans = s[left : right + 1]
        return ans

    def longestCommonPrefix(self, str):
        if not str:
            return ""
        str.sort()

        first = str[0]
        last = str[-1]

        ans = []

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(ans)
            ans.append(first[i])
        return "".join(ans)

    def isomorphicString(self, s, t):
        # your code goes here
        m1, m2 = [0] * 256, [0] * 256

        # Length of the string
        n = len(s)

        # Iterate through each character in the strings
        for i in range(n):
            # If the last seen positions of the current characters don't match, return false
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False

            # Update the last seen positions
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1

        # If all characters match, return true
        return True

    def rotateString(self, s, goal):
        if s == goal:
            return True
        str = s + s

        return goal in str

    def anagramStrings(self, s, t):

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def frequencySort(self, s):
        # your code goes here
        freqArr = []

        for i in range(26):
            freqArr.append((0, chr(i + ord("a"))))

        for ch in s:
            ind = ord(ch) - ord("a")
            freqArr[ind] = (freqArr[ind][0] + 1, ch)

        freqArr.sort(key=lambda x: (-x[0], x[1]))

        ans = []
        for freq in freqArr:
            if freq[0] > 0:
                ans.append(freq[1])

        return ans


if __name__ == "__main__":
    solution = Solution()
    str_input = input()
    reversed_str = solution.palindromeCheck(str_input)
    print(reversed_str)
