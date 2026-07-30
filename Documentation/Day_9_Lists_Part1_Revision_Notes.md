# Day 9 Revision Notes -- Lists (Part 1)

## What is a List?

-   Ordered, mutable collection of elements.
-   Can store integers, floats, strings, booleans, objects, and other
    lists.

Example:

``` python
numbers = [10, 20, 30]
```

## Why Lists?

Store multiple values in one variable.

## Internal Working

-   Variables hold references to list objects.
-   Lists store references to their elements.

## Creating Lists

``` python
[]
[1, 2, 3]
[10, "Hi", True]
[1, [2, 3], 4]
```

## Indexing

``` python
numbers[0]
numbers[-1]
```

## Slicing

``` python
numbers[start:stop:step]
numbers[1:4]
numbers[::-1]
```

-   Start included
-   Stop excluded

## Mutability

``` python
nums = [10, 20, 30]
nums[1] = 200
```

Lists can be modified.

## Nested Lists

``` python
matrix = [[1,2],[3,4]]
matrix[1][0]   # 3
```

## Common Mistakes

-   IndexError
-   Confusing indexing and slicing
-   Assuming slicing modifies the original list

## Interview Questions

1.  What is a list?
2.  Why are lists mutable?
3.  List vs String.
4.  What is indexing?
5.  What is slicing?
6.  What is a nested list?
7.  Can lists store mixed data?
8.  Do lists store values or references?
9.  Difference between numbers\[2\] and numbers\[2:3\]?
10. Why does slicing return a new list?

## Quick Revision

-   Ordered, mutable collection.
-   Stores references.
-   Supports mixed data types.
-   Index starts at 0.
-   Negative indexing starts at -1.
-   Slicing creates a new list.
