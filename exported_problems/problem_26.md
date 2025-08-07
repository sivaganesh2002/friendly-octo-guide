Calculate the product of all elements in an array except for the element at the current index.

Given an integer array nums, your task is to create a new array answer where answer[i] is the product of all elements in nums except for nums[i]. A key constraint is that you must not use the division operator.

## Input

* The function will receive one argument: nums, an array of integers.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return a new array of integers, answer, of the same length, where each element is the calculated product.

## Examples

### Example 1:

```text
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

**Explanation:**
answer[0] is 2*3*4=24, answer[1] is 1*3*4=12, and so on.

### Example 2:

```text
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

**Explanation:**
Any product that includes the 0 at index 2 will become 0. The product for index 2 itself is -1*1*-3*3=9.

## Constraints

* 2 <= nums.length <= 1000
* -30 <= nums[i] <= 30