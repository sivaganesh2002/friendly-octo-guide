Determine if a string can be segmented into a sequence of one or more dictionary words.

You are given a string s and a dictionary of strings wordDict. Your goal is to determine if s can be completely broken down into a space-separated sequence of words, where each word exists in the wordDict. Words from the dictionary can be reused.

## Input

* The function will receive two arguments: s, the string to be segmented, and wordDict, an array of strings representing the dictionary.

## Output

* Your function should return a boolean value: true if the string can be segmented, and false otherwise.

## Examples

### Example 1:

```text
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
```

**Explanation:**
The string can be segmented as "leet code".

### Example 2:

```text
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
```

**Explanation:**
The string can be segmented as "apple pen apple", reusing the word "apple".

## Constraints

* 1 <= s.length <= 300
* 1 <= wordDict.length <= 1000
* All strings in wordDict are unique.