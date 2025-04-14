class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq.keys():
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        # Step 2: Sort the frequency dictionary by values in descending order
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Extract the top-k elements
        top_k = [item[0] for item in sorted_freq[:k]]
        
        return top_k


            