# Initial list and rotation steps
nums = [1, 2, 3, 4, 5]
k = 2

# 1. Normalize k in case it's larger than the list length
k = k % len(nums)

# 2. Perform rotation: (last k elements) + (everything except last k)
rotated_list = nums[-k:] + nums[:-k]

print(rotated_list)  # Output: [4, 5, 1, 2, 3]
