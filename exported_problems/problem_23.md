Determine if a given binary tree is a valid Binary Search Tree (BST).

A binary tree is a valid BST if it satisfies three conditions for every node: 1) The node's value is greater than all values in its left subtree. 2) The node's value is less than all values in its right subtree. 3) Both the left and right subtrees are themselves valid BSTs.

## Input

* The function will receive one argument: root, which is an array representing a binary tree in level-order traversal. null values in the array represent empty nodes.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return a boolean value: true if the tree is a valid BST, and false otherwise.

## Examples

### Example 1:

```text
Input: root = [2, 1, 3]
Output: true
```

**Explanation:**
The root (2) is greater than its left child (1) and less than its right child (3).

### Example 2:

```text
Input: root = [5, 1, 4, null, null, 3, 6]
Output: false
```

**Explanation:**
The node with value 4 is in the right subtree of the root (5), but 4 is not greater than 5, violating the BST property.

## Constraints

* The number of nodes in the tree is in the range [1, 1000].
* -1000 <= Node.val <= 1000