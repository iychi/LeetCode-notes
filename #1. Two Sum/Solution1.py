# brute force: time: O(n^2)  space:O(1)
def twoSum(nums: list[int], target: int) -> list[int]:    
    # edge case
    if not nums:
        return []

    # iterate each number in nums and check every number after nums[i]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # the sum of nums[i] and nums[j] == target, return indices
            if nums[i] + nums[j] == target:
                return [i, j]


n1, t1 = [2,7,11,15], 9  # [0,1]
n2, t2 = [3,2,4], 6  # [1,2]
n3, t3 = [3,3], 6  # [0,1]

print(twoSum(n1,t1))
print(twoSum(n2,t2))
print(twoSum(n3,t3))