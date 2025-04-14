class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for i in range(len(words)):
            if words[i] in freq.keys():
                freq[words[i]] += 1
            else:
                freq[words[i]] = 1

        # Step 2: Sort the frequency dictionary by values in descending order
        sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Step 3: Extract the top-k elements
        top_k = [item[0] for item in sorted_freq[:k]]
        
        return top_k
            