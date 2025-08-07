Find the area of the largest rectangle that can be formed within a histogram.

Given an array of integers heights representing the bar heights of a histogram (where each bar has a width of 1), your task is to find the area of the largest possible rectangle that can be drawn within this histogram.

## Input

* The function will receive one argument: heights, an array of non-negative integers.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return an integer representing the area of the largest rectangle.

## Examples

### Example 1:

```text
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
```

**Explanation:**
The largest rectangle has a height of 5 and spans 2 bars (the ones with heights 5 and 6), for an area of 5 * 2 = 10.

### Example 2:

```text
Input: heights = [2, 4]
Output: 4
```

**Explanation:**
The largest rectangle can be the bar of height 4 (area 41=4) or a rectangle of height 2 spanning both bars (area 22=4).

## Constraints

* 1 <= heights.length <= 1000
* 0 <= heights[i] <= 1000