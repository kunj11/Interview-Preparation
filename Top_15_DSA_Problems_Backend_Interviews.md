
# Top 15 DSA Problems That Cover 80% of Backend Interviews

A focused list of **high-impact algorithm problems** for experienced backend engineers preparing for **non‑FAANG interviews**.

Goal:

```
Practice fewer problems
But master the patterns deeply
```

---

## Pattern Coverage Map

| Pattern | Covered By |
|---|---|
| Arrays + HashMap | Two Sum |
| Sliding Window | Longest Substring Without Repeating |
| Stack | Valid Parentheses |
| Linked List | Reverse Linked List |
| Two Pointer | Container With Most Water |
| Binary Search | Binary Search |
| Trees DFS | Maximum Depth of Binary Tree |
| Trees BFS | Level Order Traversal |
| Heap | Top K Frequent Elements |
| Dynamic Programming | Maximum Subarray |
| Cycle Detection | Linked List Cycle |
| Backtracking | Subsets |
| Array Greedy | Product of Array Except Self |
| Hashing + Sorting | Group Anagrams |
| Monotonic Stack | Daily Temperatures |

---

## 1. Two Sum

**Pattern:** HashMap

Example

```
nums = [2,7,11,15]
target = 9
Output = [0,1]
```

Key Idea

```
Store numbers in hashmap
Check if target - current exists
```

---

## 2. Longest Substring Without Repeating Characters

**Pattern:** Sliding Window

Example

```
Input: "abcabcbb"
Output: 3
```

Idea

```
Expand window
Shrink when duplicate appears
```

---

## 3. Valid Parentheses

**Pattern:** Stack

Example

```
Input: "()[]{}"
Output: True
```

---

## 4. Reverse Linked List

**Pattern:** Pointer manipulation

Visualization

```
1 → 2 → 3 → 4
becomes
4 → 3 → 2 → 1
```

---

## 5. Container With Most Water

**Pattern:** Two Pointers

```
L →           ← R
[1,8,6,2,5,4,8,3,7]
```

---

## 6. Binary Search

**Pattern:** Binary Search

```
mid = (left + right) // 2
```

---

## 7. Maximum Depth of Binary Tree

**Pattern:** DFS

```
depth = 1 + max(leftDepth, rightDepth)
```

---

## 8. Binary Tree Level Order Traversal

**Pattern:** BFS

```
Use queue for level traversal
```

---

## 9. Top K Frequent Elements

**Pattern:** Heap

```
Count frequency + use heap
```

---

## 10. Maximum Subarray

**Pattern:** Dynamic Programming (Kadane)

```
current = max(num, current + num)
```

---

## 11. Linked List Cycle

**Pattern:** Fast / Slow Pointer

```
If slow == fast → cycle exists
```

---

## 12. Subsets

**Pattern:** Backtracking

Example

```
nums = [1,2]
Output
[]
[1]
[2]
[1,2]
```

---

## 13. Product of Array Except Self

**Pattern:** Prefix / Suffix arrays

```
nums = [1,2,3,4]
Output
[24,12,8,6]
```

---

## 14. Group Anagrams

**Pattern:** HashMap + Sorting

Example

```
["eat","tea","tan","ate","nat","bat"]
```

---

## 15. Daily Temperatures

**Pattern:** Monotonic Stack

Example

```
[73,74,75,71,69,72,76,73]
```

---

## Practice Strategy

```
Week 1 → solve all
Week 2 → solve again
Week 3 → timed practice
Week 4 → random order
```

Master these problems and you will recognize most interview patterns quickly.
