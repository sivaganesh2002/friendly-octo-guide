Check if a given string is a palindrome, ignoring case and non-alphanumeric characters.

A phrase is a palindrome if it reads the same forwards and backward. Your task is to verify this for a given string after converting all uppercase letters into lowercase and removing all non-alphanumeric characters (i.e., keeping only letters and numbers).

## Input

* The function will receive one argument: s, a string.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return a boolean value: true if the processed string is a palindrome, and false otherwise.

## Examples

### Example 1:

```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

**Explanation:**
After processing, the string becomes "amanaplanacanalpanama", which is a palindrome.

### Example 2:

```text
Input: s = "race a car"
Output: false
```

**Explanation:**
After processing, the string becomes "raceacar", which is not a palindrome.

## Constraints

* 1 <= s.length <= 1000
* s consists only of printable ASCII characters.