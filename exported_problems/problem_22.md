Find the maximum depth of a binary tree.

The maximum depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node. A leaf node is a node with no children. An empty tree has a depth of 0.

## Input

* The function will receive one argument: root, an array representing a binary tree in level-order traversal. null values signify empty branches.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return an integer representing the maximum depth of the tree.

## Examples

### Example 1:

```text
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3
```

**Explanation:**
The longest path goes from root (3) to its child (20) to its child (15 or 7).

### Example 2:

```text
Input: root = [1, null, 2]
Output: 2
```

**Explanation:**
The longest path is from root (1) to its right child (2).

## Constraints

* The number of nodes in the tree is in the range [0, 1000].
* -100 <= Node.val <= 100