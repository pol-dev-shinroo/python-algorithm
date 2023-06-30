class Solution:
    def uniqueOccurrences(self, arr):
        freq = {}

        for i in range(len(arr)):
            freq[arr[i]] = freq.get(i, 0) + 1

        freq_set = set(freq.values())

        return len(freq) == len(freq_set)
