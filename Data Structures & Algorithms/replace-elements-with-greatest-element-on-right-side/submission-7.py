class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightmax = -1
        for i in range(n - 1, -1, -1):
            tmp = arr[i]
            arr[i] = rightmax
            rightmax = max(rightmax, tmp)
        return arr


        