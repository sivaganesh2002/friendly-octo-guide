Generate a list of strings from 1 to n based on divisibility by 3 and 5.

Your task is to generate a sequence of strings representing the numbers from 1 to n. However, for multiples of three, use the string "Fizz" instead of the number. For multiples of five, use "Buzz". For numbers which are multiples of both three and five, use "FizzBuzz".

## Input

* The function will receive one argument: n, an integer.

  ```python
  def missingNumber(nums: List[int]) -> int
  ```

## Output

* Your function should return an array of strings representing the generated sequence.

## Examples

### Example 1:

```text
Input: n = 3
Output: ["1", "2", "Fizz"]
```

**Explanation:**
1 and 2 are printed as numbers, while 3 is a multiple of 3.

### Example 2:

```text
Input: n = 15
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
```

**Explanation:**
The sequence is generated up to 15, with special strings for multiples of 3, 5, and both.

## Constraints

* 1 <= n <= 1000