Find the length of the longest substring within a given string that does not contain repeating characters.

Given a string s, you need to find the length of the longest possible substring (a contiguous block of characters) that has no repeating characters.

## Input

* The function will receive one argument: s, a string.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return an integer representing the length of the longest substring found.

## Examples

### Example 1:

```text
Input: s = "abcabcbb"
Output: 3
```

**Explanation:**
The longest substring without repeating characters is "abc", which has a length of 3.

### Example 2:

```text
Input: s = "pwwkew"
Output: 3
```

**Explanation:**
The longest substring is "wke" with a length of 3. Note that "pwke" is a subsequence, not a substring.

## Constraints

* 0 <= s.length <= 1000
* s consists of English letters, digits, symbols, and spaces.