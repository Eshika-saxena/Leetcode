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
