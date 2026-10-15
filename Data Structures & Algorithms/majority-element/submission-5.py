class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_val=0
        max_cnt=0
        hash_map={}

        for i in range(len(nums)):
            hash_map[nums[i]]=1+hash_map.get(nums[i],0)

        
        for val,current_cnt in hash_map.items():
            if current_cnt>=max_cnt:
                max_val=val
                max_cnt=current_cnt

        
        return max_val

        