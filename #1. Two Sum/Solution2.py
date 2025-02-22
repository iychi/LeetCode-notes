def twoSum(nums: list[int], target: int) -> list[int]:
    
    # edge case
    if not nums:
        return []
    
    # hashmap: time: O(n)  space:O(n)
    # store difference of each number with target in dict {diff:i}
    # check every other number to find the one same as difference
    diff_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in diff_map and i != diff_map[nums[i]]:
            return [i, diff_map[nums[i]]]
        diff_map[diff] = i


n1, t1 = [2,7,11,15], 9  # [0,1]
n2, t2 = [3,2,4], 6  # [1,2]
n3, t3 = [3,3], 6  # [0,1]

print(twoSum(n1,t1))
print(twoSum(n2,t2))
print(twoSum(n3,t3))