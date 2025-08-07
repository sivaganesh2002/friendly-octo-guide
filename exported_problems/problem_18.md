Find the longest contiguous substring that is also a palindrome.

Given a string s, your task is to find and return the longest substring within s that is a palindrome. A string is a palindrome if it reads the same forwards and backwards. If there are multiple longest palindromic substrings, returning any one of them is acceptable.

## Input

* The function will receive one argument: s, a string.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return a string that is the longest palindromic substring.

## Examples

### Example 1:

```text
Input: s = "babad"
Output: "bab"
```

**Explanation:**
"aba" is also a valid answer as it's also a palindrome of length 3.

### Example 2:

```text
Input: s = "cbbd"
Output: "bb"
```

**Explanation:**
"bb" is the longest palindromic substring.

## Constraints

* 1 <= s.length <= 1000
* s consist of only digits and English letters.