Intuition:
Create a dictionary by name "mapp" and store each distinct element from the list as key and its count as value.
Then compare the value of each key with the length of the list. If the value is greater than the length of the list divided by 3, then append the key to the list "result" and then return res.

Approach:
1.Create a dictionary by name "mapp".
2.Traverse through the list "nums".
3.If the element is already present in the dictionary, then increment its value by 1.
4.Else, add the element as key and its value as 1.
5.Create an empty list "result".
6.Traverse through the dictionary "mapp".
7.If the value of a key is greater than "(n/3)" , then append the key to the list "result".
8.Return the list "result".

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/Eshika-saxena/Leetcode/tree/master/0004-median-of-two-sorted-arrays) |
| [0026-remove-duplicates-from-sorted-array](https://github.com/Eshika-saxena/Leetcode/tree/master/0026-remove-duplicates-from-sorted-array) |
| [0034-find-first-and-last-position-of-element-in-sorted-array](https://github.com/Eshika-saxena/Leetcode/tree/master/0034-find-first-and-last-position-of-element-in-sorted-array) |
| [0041-first-missing-positive](https://github.com/Eshika-saxena/Leetcode/tree/master/0041-first-missing-positive) |
| [0042-trapping-rain-water](https://github.com/Eshika-saxena/Leetcode/tree/master/0042-trapping-rain-water) |
| [0136-single-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0136-single-number) |
| [0169-majority-element](https://github.com/Eshika-saxena/Leetcode/tree/master/0169-majority-element) |
| [0219-contains-duplicate-ii](https://github.com/Eshika-saxena/Leetcode/tree/master/0219-contains-duplicate-ii) |
| [0260-single-number-iii](https://github.com/Eshika-saxena/Leetcode/tree/master/0260-single-number-iii) |
| [0287-find-the-duplicate-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0287-find-the-duplicate-number) |
| [0347-top-k-frequent-elements](https://github.com/Eshika-saxena/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/Eshika-saxena/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/Eshika-saxena/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [0448-find-all-numbers-disappeared-in-an-array](https://github.com/Eshika-saxena/Leetcode/tree/master/0448-find-all-numbers-disappeared-in-an-array) |
| [0485-max-consecutive-ones](https://github.com/Eshika-saxena/Leetcode/tree/master/0485-max-consecutive-ones) |
| [1556-make-two-arrays-equal-by-reversing-subarrays](https://github.com/Eshika-saxena/Leetcode/tree/master/1556-make-two-arrays-equal-by-reversing-subarrays) |
| [1603-running-sum-of-1d-array](https://github.com/Eshika-saxena/Leetcode/tree/master/1603-running-sum-of-1d-array) |
| [1813-maximum-erasure-value](https://github.com/Eshika-saxena/Leetcode/tree/master/1813-maximum-erasure-value) |
| [1927-maximum-ascending-subarray-sum](https://github.com/Eshika-saxena/Leetcode/tree/master/1927-maximum-ascending-subarray-sum) |
| [2113-find-the-kth-largest-integer-in-the-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2113-find-the-kth-largest-integer-in-the-array) |
| [2163-kth-distinct-string-in-an-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2163-kth-distinct-string-in-an-array) |
| [2210-find-target-indices-after-sorting-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2210-find-target-indices-after-sorting-array) |
## Hash Table
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/Eshika-saxena/Leetcode/tree/master/0003-longest-substring-without-repeating-characters) |
| [0041-first-missing-positive](https://github.com/Eshika-saxena/Leetcode/tree/master/0041-first-missing-positive) |
| [0169-majority-element](https://github.com/Eshika-saxena/Leetcode/tree/master/0169-majority-element) |
| [0202-happy-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0202-happy-number) |
| [0219-contains-duplicate-ii](https://github.com/Eshika-saxena/Leetcode/tree/master/0219-contains-duplicate-ii) |
| [0347-top-k-frequent-elements](https://github.com/Eshika-saxena/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/Eshika-saxena/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/Eshika-saxena/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [0448-find-all-numbers-disappeared-in-an-array](https://github.com/Eshika-saxena/Leetcode/tree/master/0448-find-all-numbers-disappeared-in-an-array) |
| [1556-make-two-arrays-equal-by-reversing-subarrays](https://github.com/Eshika-saxena/Leetcode/tree/master/1556-make-two-arrays-equal-by-reversing-subarrays) |
| [1813-maximum-erasure-value](https://github.com/Eshika-saxena/Leetcode/tree/master/1813-maximum-erasure-value) |
| [2163-kth-distinct-string-in-an-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2163-kth-distinct-string-in-an-array) |
## Sorting
|  |
| ------- |
| [0169-majority-element](https://github.com/Eshika-saxena/Leetcode/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/Eshika-saxena/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/Eshika-saxena/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/Eshika-saxena/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [1556-make-two-arrays-equal-by-reversing-subarrays](https://github.com/Eshika-saxena/Leetcode/tree/master/1556-make-two-arrays-equal-by-reversing-subarrays) |
| [2113-find-the-kth-largest-integer-in-the-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2113-find-the-kth-largest-integer-in-the-array) |
| [2210-find-target-indices-after-sorting-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2210-find-target-indices-after-sorting-array) |
## String
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/Eshika-saxena/Leetcode/tree/master/0003-longest-substring-without-repeating-characters) |
| [0005-longest-palindromic-substring](https://github.com/Eshika-saxena/Leetcode/tree/master/0005-longest-palindromic-substring) |
| [0125-valid-palindrome](https://github.com/Eshika-saxena/Leetcode/tree/master/0125-valid-palindrome) |
| [0412-fizz-buzz](https://github.com/Eshika-saxena/Leetcode/tree/master/0412-fizz-buzz) |
| [1128-remove-all-adjacent-duplicates-in-string](https://github.com/Eshika-saxena/Leetcode/tree/master/1128-remove-all-adjacent-duplicates-in-string) |
| [2021-remove-all-occurrences-of-a-substring](https://github.com/Eshika-saxena/Leetcode/tree/master/2021-remove-all-occurrences-of-a-substring) |
| [2113-find-the-kth-largest-integer-in-the-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2113-find-the-kth-largest-integer-in-the-array) |
| [2163-kth-distinct-string-in-an-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2163-kth-distinct-string-in-an-array) |
| [2470-removing-stars-from-a-string](https://github.com/Eshika-saxena/Leetcode/tree/master/2470-removing-stars-from-a-string) |
| [3447-clear-digits](https://github.com/Eshika-saxena/Leetcode/tree/master/3447-clear-digits) |
## Counting
|  |
| ------- |
| [0169-majority-element](https://github.com/Eshika-saxena/Leetcode/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/Eshika-saxena/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [2163-kth-distinct-string-in-an-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2163-kth-distinct-string-in-an-array) |
## Binary Search
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/Eshika-saxena/Leetcode/tree/master/0004-median-of-two-sorted-arrays) |
| [0034-find-first-and-last-position-of-element-in-sorted-array](https://github.com/Eshika-saxena/Leetcode/tree/master/0034-find-first-and-last-position-of-element-in-sorted-array) |
| [0287-find-the-duplicate-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0287-find-the-duplicate-number) |
| [0349-intersection-of-two-arrays](https://github.com/Eshika-saxena/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/Eshika-saxena/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [2210-find-target-indices-after-sorting-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2210-find-target-indices-after-sorting-array) |
## Divide and Conquer
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/Eshika-saxena/Leetcode/tree/master/0004-median-of-two-sorted-arrays) |
| [0169-majority-element](https://github.com/Eshika-saxena/Leetcode/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/Eshika-saxena/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [2113-find-the-kth-largest-integer-in-the-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2113-find-the-kth-largest-integer-in-the-array) |
## Two Pointers
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/Eshika-saxena/Leetcode/tree/master/0005-longest-palindromic-substring) |
| [0026-remove-duplicates-from-sorted-array](https://github.com/Eshika-saxena/Leetcode/tree/master/0026-remove-duplicates-from-sorted-array) |
| [0042-trapping-rain-water](https://github.com/Eshika-saxena/Leetcode/tree/master/0042-trapping-rain-water) |
| [0125-valid-palindrome](https://github.com/Eshika-saxena/Leetcode/tree/master/0125-valid-palindrome) |
| [0202-happy-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0202-happy-number) |
| [0287-find-the-duplicate-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0287-find-the-duplicate-number) |
| [0349-intersection-of-two-arrays](https://github.com/Eshika-saxena/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/Eshika-saxena/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
## Dynamic Programming
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/Eshika-saxena/Leetcode/tree/master/0005-longest-palindromic-substring) |
| [0042-trapping-rain-water](https://github.com/Eshika-saxena/Leetcode/tree/master/0042-trapping-rain-water) |
## Math
|  |
| ------- |
| [0007-reverse-integer](https://github.com/Eshika-saxena/Leetcode/tree/master/0007-reverse-integer) |
| [0202-happy-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0202-happy-number) |
| [0412-fizz-buzz](https://github.com/Eshika-saxena/Leetcode/tree/master/0412-fizz-buzz) |
## Simulation
|  |
| ------- |
| [0412-fizz-buzz](https://github.com/Eshika-saxena/Leetcode/tree/master/0412-fizz-buzz) |
| [2021-remove-all-occurrences-of-a-substring](https://github.com/Eshika-saxena/Leetcode/tree/master/2021-remove-all-occurrences-of-a-substring) |
| [2470-removing-stars-from-a-string](https://github.com/Eshika-saxena/Leetcode/tree/master/2470-removing-stars-from-a-string) |
| [3447-clear-digits](https://github.com/Eshika-saxena/Leetcode/tree/master/3447-clear-digits) |
## Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/Eshika-saxena/Leetcode/tree/master/0042-trapping-rain-water) |
| [1128-remove-all-adjacent-duplicates-in-string](https://github.com/Eshika-saxena/Leetcode/tree/master/1128-remove-all-adjacent-duplicates-in-string) |
| [2021-remove-all-occurrences-of-a-substring](https://github.com/Eshika-saxena/Leetcode/tree/master/2021-remove-all-occurrences-of-a-substring) |
| [2470-removing-stars-from-a-string](https://github.com/Eshika-saxena/Leetcode/tree/master/2470-removing-stars-from-a-string) |
| [3447-clear-digits](https://github.com/Eshika-saxena/Leetcode/tree/master/3447-clear-digits) |
## Monotonic Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/Eshika-saxena/Leetcode/tree/master/0042-trapping-rain-water) |
## Bit Manipulation
|  |
| ------- |
| [0136-single-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0136-single-number) |
| [0260-single-number-iii](https://github.com/Eshika-saxena/Leetcode/tree/master/0260-single-number-iii) |
| [0287-find-the-duplicate-number](https://github.com/Eshika-saxena/Leetcode/tree/master/0287-find-the-duplicate-number) |
## Tree
|  |
| ------- |
| [0100-same-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0100-same-tree) |
| [0102-binary-tree-level-order-traversal](https://github.com/Eshika-saxena/Leetcode/tree/master/0102-binary-tree-level-order-traversal) |
| [0104-maximum-depth-of-binary-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0104-maximum-depth-of-binary-tree) |
| [0111-minimum-depth-of-binary-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0111-minimum-depth-of-binary-tree) |
| [0199-binary-tree-right-side-view](https://github.com/Eshika-saxena/Leetcode/tree/master/0199-binary-tree-right-side-view) |
## Breadth-First Search
|  |
| ------- |
| [0100-same-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0100-same-tree) |
| [0102-binary-tree-level-order-traversal](https://github.com/Eshika-saxena/Leetcode/tree/master/0102-binary-tree-level-order-traversal) |
| [0104-maximum-depth-of-binary-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0104-maximum-depth-of-binary-tree) |
| [0111-minimum-depth-of-binary-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0111-minimum-depth-of-binary-tree) |
| [0199-binary-tree-right-side-view](https://github.com/Eshika-saxena/Leetcode/tree/master/0199-binary-tree-right-side-view) |
## Binary Tree
|  |
| ------- |
| [0100-same-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0100-same-tree) |
| [0102-binary-tree-level-order-traversal](https://github.com/Eshika-saxena/Leetcode/tree/master/0102-binary-tree-level-order-traversal) |
| [0104-maximum-depth-of-binary-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0104-maximum-depth-of-binary-tree) |
| [0111-minimum-depth-of-binary-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0111-minimum-depth-of-binary-tree) |
| [0199-binary-tree-right-side-view](https://github.com/Eshika-saxena/Leetcode/tree/master/0199-binary-tree-right-side-view) |
## Depth-First Search
|  |
| ------- |
| [0100-same-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0100-same-tree) |
| [0104-maximum-depth-of-binary-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0104-maximum-depth-of-binary-tree) |
| [0111-minimum-depth-of-binary-tree](https://github.com/Eshika-saxena/Leetcode/tree/master/0111-minimum-depth-of-binary-tree) |
| [0199-binary-tree-right-side-view](https://github.com/Eshika-saxena/Leetcode/tree/master/0199-binary-tree-right-side-view) |
## Prefix Sum
|  |
| ------- |
| [1603-running-sum-of-1d-array](https://github.com/Eshika-saxena/Leetcode/tree/master/1603-running-sum-of-1d-array) |
## Heap (Priority Queue)
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/Eshika-saxena/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [2113-find-the-kth-largest-integer-in-the-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2113-find-the-kth-largest-integer-in-the-array) |
## Quickselect
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/Eshika-saxena/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [2113-find-the-kth-largest-integer-in-the-array](https://github.com/Eshika-saxena/Leetcode/tree/master/2113-find-the-kth-largest-integer-in-the-array) |
## Bucket Sort
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/Eshika-saxena/Leetcode/tree/master/0347-top-k-frequent-elements) |
## Sliding Window
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/Eshika-saxena/Leetcode/tree/master/0003-longest-substring-without-repeating-characters) |
| [0219-contains-duplicate-ii](https://github.com/Eshika-saxena/Leetcode/tree/master/0219-contains-duplicate-ii) |
| [1813-maximum-erasure-value](https://github.com/Eshika-saxena/Leetcode/tree/master/1813-maximum-erasure-value) |
<!---LeetCode Topics End-->