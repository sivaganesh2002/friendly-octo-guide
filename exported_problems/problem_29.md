Combine two sorted integer arrays into a single sorted array.

You are given two integer arrays, nums1 and nums2, both sorted in non-decreasing order. Your task is to merge them into a single, new array that is also sorted in non-decreasing order.

## Input

* The function will receive two arguments: nums1 and nums2, both of which are sorted arrays of integers.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return a new array of integers containing all elements from nums1 and nums2 in sorted order.

## Examples

### Example 1:

```text
Input: nums1 = [1, 2, 4], nums2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

**Explanation:**
The elements from both arrays are combined and sorted.

### Example 2:

```text
Input: nums1 = [], nums2 = [0]
Output: [0]
```

**Explanation:**
Merging an empty array with another results in the second array.

## Constraints

* 0 <= nums1.length, nums2.length <= 500
* -1000 <= nums1[i], nums2[i] <= 1000