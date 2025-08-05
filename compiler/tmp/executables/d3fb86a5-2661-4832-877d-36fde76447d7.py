def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Read input
nums = list(map(int, input().strip().split()))
print(missing_number(nums))