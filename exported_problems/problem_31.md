Find the indices of two numbers in an array that add up to a specific target value.

Given an array of integers nums and an integer target, your task is to find two numbers within the array that sum up to the target value. You must not use the same element twice, and it's guaranteed that exactly one solution exists for every test case.

## Input

* The function will receive two arguments: nums, an array of integers, and target, an integer.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return an array containing the two zero-based indices of the numbers that sum to the target.

## Examples

### Example 1:

```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

**Explanation:**
The numbers at index 0 (value 2) and index 1 (value 7) add up to 9.

### Example 2:

```text
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

**Explanation:**
The numbers at index 1 (value 2) and index 2 (value 4) add up to 6.

## Constraints

* 2 <= nums.length <= 1000
* -1000 <= nums[i] <= 1000
* -1000 <= target <= 1000