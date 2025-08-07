Calculate the total amount of rainwater that can be trapped between vertical bars of a histogram.

You are given an array of non-negative integers height representing an elevation map where the width of each bar is 1. Your task is to compute how many units of water can be trapped in the depressions formed by these bars after it rains.

## Input

* The function will receive one argument: height, an array of non-negative integers.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return a single integer representing the total units of trapped water.

## Examples

### Example 1:

```text
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
```

**Explanation:**
The bars form containers that can hold a total of 6 units of water.

### Example 2:

```text
Input: height = [4, 2, 0, 3, 2, 5]
Output: 9
```

**Explanation:**
The large container between the bars of height 4 and 5 traps the most water.

## Constraints

* n == height.length
* 1 <= n <= 1000
* 0 <= height[i] <= 1000