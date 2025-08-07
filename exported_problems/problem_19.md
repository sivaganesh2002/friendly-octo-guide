Merge k sorted linked lists (given as arrays) into one sorted list.

You are given an array of arrays called lists. Each inner array is sorted in ascending order. Your goal is to merge all of these arrays into a single, comprehensive sorted array.

## Input

* The function will receive one argument: lists, an array of sorted integer arrays.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return a single array containing all elements from all input arrays, sorted in ascending order.

## Examples

### Example 1:

```text
Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

**Explanation:**
All elements from the three input arrays are combined into one sorted array.

### Example 2:

```text
Input: lists = [[]]
Output: []
```

**Explanation:**
Merging a list containing one empty list results in an empty list.

## Constraints

* k == lists.length
* 0 <= k <= 1000
* 0 <= lists[i].length <= 500