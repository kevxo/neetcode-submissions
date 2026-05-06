# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)


    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs

        m = (s + e) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)
        self.merge(pairs, s, m, e)

        return pairs

    def merge(self, arr, s, m, e):
        l = arr[s: m+1]
        r = arr[m + 1: e + 1]

        i = 0 # index for l
        j = 0 # index for r
        k = s # index for arr

        # merge the two sorted halfs
        while i < len(l) and j < len(r):
            if l[i].key <= r[j].key:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1

            k += 1

        # one of the two halfs will have elements remaining
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1