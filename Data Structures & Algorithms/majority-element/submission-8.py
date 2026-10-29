class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        max_count=0
        max_val=0

        for num in nums:
            hash_map[num]=1+hash_map.get(num,0)

        for val,count in hash_map.items():
            if count >=max_count:
                max_count=count
                max_val=val

        return max_val