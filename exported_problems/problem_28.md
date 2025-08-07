Find the single missing number from a sequence containing all numbers from 0 to n.

You are given an array nums containing n distinct numbers taken from the range [0, 1, 2, ..., n]. Because the array has only n numbers, exactly one number from that range is missing. Your goal is to find it.

## Input

* The function will receive one argument: nums, an array of distinct integers.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return the single integer that is missing from the complete range [0, n].

## Examples

### Example 1:

```text
Input: nums = [3, 0, 1]
Output: 2
```

**Explanation:**
The array has 3 elements, so the range is [0, 3]. The number 2 is missing.

### Example 2:

```text
Input: nums = [0, 1]
Output: 2
```

**Explanation:**
The array has 2 elements, so the range is [0, 2]. The number 2 is missing.

## Constraints

* n == nums.length
* 1 <= n <= 1000
* All the numbers of nums are unique.