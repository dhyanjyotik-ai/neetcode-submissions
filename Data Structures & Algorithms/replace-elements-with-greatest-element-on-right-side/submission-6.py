class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            rightmax = -1
            for j in range(i + 1, n):
                rightmax = max(rightmax, arr[j])
            arr[i] = rightmax
        return arr


        