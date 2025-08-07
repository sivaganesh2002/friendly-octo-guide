import ast

def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Correctly handle input like: [0, 1, 3]
nums = ast.literal_eval(input())

print(missingNumber(nums))