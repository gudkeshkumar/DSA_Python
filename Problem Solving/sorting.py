class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n):
            minIndex = i

            for j in range(i+1, n):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            if minIndex != i:
                nums[minIndex], nums[i] = nums[i], nums[minIndex]

        return nums

    def bubbleSort(self, nums):
        n = len(nums)

        for i in range(n):

            didswap = 0
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

                    didswap = 1
            if didswap == 0:
                break
        return nums

    def insertionSort(self, nums):
        n = len(nums)

        for i in range(n):
            j = i

            while j > 0 and nums[j - 1] > nums[j]:
                temp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = temp
                j -= 1
        return nums

    def quickSort(self, nums):
        n = len(nums)
        self.quickSortHelper(nums, 0, n - 1)
        return nums

    def quickSortHelper(self, arr, low, high):

        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSortHelper(arr, low, pIndex - 1)
            self.quickSortHelper(arr, pIndex + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1

            while arr[j] > pivot and j >= low - 1:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def mergeSort(self, nums):
        n = len(nums)
        self.msHelper(nums, 0, n - 1)
        return nums

    def msHelper(self, arr, low, high):

        if low >= high:
            return
        mid = (low + high) // 2
        self.msHelper(arr, low, mid)
        self.msHelper(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]


if __name__ == "__main__":
    input_str = input()
    int_list = [int(x) for x in input_str.split()]
    # Creating an instance of Solution class
    sol = Solution()

    ans = sol.insertionSort(int_list)

    print("The sorted array is:", ans)
