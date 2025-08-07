Rotate the elements of an array to the right by a specified number of steps.

Given an array nums and a non-negative integer k, your task is to rotate the array's elements to the right by k steps. This means the last k elements will move to the front, and the other elements will be shifted back.

## Input

* The function will receive two arguments: nums, an array of integers, and k, a non-negative integer representing the number of rotations.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* The function should modify the nums array in-place and return the modified array.

## Examples

### Example 1:

```text
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
```

**Explanation:**
After 1 rotation: [7, 1, 2, 3, 4, 5, 6]. After 2: [6, 7, 1, 2, 3, 4, 5]. After 3: [5, 6, 7, 1, 2, 3, 4].

### Example 2:

```text
Input: nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
```

**Explanation:**
The last two elements [3, 99] move to the front.

## Constraints

* 1 <= nums.length <= 1000
* -1000 <= nums[i] <= 1000
* 0 <= k <= 1000