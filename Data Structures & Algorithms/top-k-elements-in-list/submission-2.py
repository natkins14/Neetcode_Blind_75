class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = {}

        for i in nums:

            if i in result:

                result[i] += 1
                
            else:
                result[i] = 1

        counts = Counter(result)

        most_common = counts.most_common(k)

        result = [item for item, count in most_common]

        return result        

