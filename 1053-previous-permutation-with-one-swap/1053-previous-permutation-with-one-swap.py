class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2

        # Find the rightmost occurrence of a number that can be swapped
        # with a smaller number to its right
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1

            # Find the largest number smaller than arr[i] to swap with
            while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
                j -= 1

            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

        return arr