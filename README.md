# HackerRank 3rd Semester Algorithm Portfolio

## Student Details

- Name: Namith kumar B V
- Semester: 3rd Semester CSE
- USN/Student ID:R25EF157
- HackerRank Profile: https://www.hackerrank.com/profile/na_myth77
- GitHub Profile: https://github.com/namithkumar2607-coder

## Introduction

This repository contains my HackerRank algorithm practice for the 3rd semester. The portfolio includes five required algorithm problems. Each solution is implemented in Python with a focus on correct output, efficient algorithms, and time and space complexity.

## Problems Completed

| No. | Problem | Approach | Time Complexity | Space Complexity |
|---|---|---|---|---|
| 1 | Mini-Max Sum | Find total sum, minimum and maximum | O(N) | O(1) |
| 2 | Birthday Cake Candles | Find maximum and count occurrences | O(N) | O(1) |
| 3 | Insertion Sort Part 1 | Shift elements and insert the last value | O(N) | O(1) |
| 4 | Binary Search | Repeatedly divide sorted array into halves | O(log N) | O(1) |
| 5 | Mark and Toys | Sort prices and greedily buy cheapest toys | O(N log N) | O(N) |

## 1. Mini-Max Sum

### Approach
Calculate the total sum of all elements. Find the minimum and maximum values. The minimum sum is obtained by subtracting the maximum value from the total, and the maximum sum is obtained by subtracting the minimum value.

### Complexity
- Time: O(N)
- Space: O(1)

### Solution
01-Mini-Max-Sum/solution.py

## 2. Birthday Cake Candles

### Approach
Find the maximum candle height and count how many candles have that height.

### Complexity
- Time: O(N)
- Space: O(1)

### Solution
02-Birthday-Cake-Candles/solution.py

## 3. Insertion Sort Part 1

### Approach
Store the last element and compare it with the elements before it. Shift larger elements one position to the right until the correct position is found.

### Complexity
- Time: O(N)
- Space: O(1)

### Solution
03-Insertion-Sort-Part-1/solution.py

## 4. Binary Search

### Approach
The array must be sorted. The middle element is checked against the target. If the target is larger, search the right half; otherwise search the left half. Continue until the element is found or the search range becomes empty.

### Complexity
- Time: O(log N)
- Space: O(1)

### Solution
04-Binary-Search/solution.py

## 5. Mark and Toys

### Approach
Sort the toy prices in ascending order and buy the cheapest toys first while staying within the given budget.

### Complexity
- Time: O(N log N)
- Space: O(N)

### Solution
05-Mark-and-Toys/solution.py

## Summary

These five problems helped me practice arrays, sorting, searching, greedy algorithms, and complexity analysis. I focused on writing simple and efficient Python solutions and understanding the time and space requirements of each algorithm.

## Evidence

Evidence of accepted HackerRank submissions and the HackerRank profile will be included as screenshots in the final report.
