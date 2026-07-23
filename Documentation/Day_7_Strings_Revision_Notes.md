# Day 7 Revision Notes -- Strings

## String

A string is a sequence of characters enclosed in quotes.

Examples:

``` python
"Python"
'Hello'
```

## Memory

Variables refer to string objects.

## Indexing

``` text
P y t h o n
0 1 2 3 4 5
```

`word[0] -> P`

## Negative Indexing

``` text
-6 -5 -4 -3 -2 -1
```

`word[-1] -> n`

## Slicing

``` python
word[start:stop:step]
```

Examples:

``` python
word[0:3]
word[2:5]
word[::2]
word[::-1]
```

-   Start included
-   Stop excluded

## Immutability

Strings cannot be changed.

``` python
word = "Python"
# word[0] = "J" -> TypeError
```

Python creates a new string object instead.

## ASCII & Unicode

-   ASCII stores basic English characters.
-   Unicode supports almost all languages and symbols.

## Interview Questions

1.  What is a string?
2.  What is indexing?
3.  What is negative indexing?
4.  What is slicing?
5.  Why are strings immutable?
6.  Difference between indexing and slicing.
7.  Explain `[::-1]`.
8.  ASCII vs Unicode.
9.  How are strings stored?
10. Why can't strings be modified?

## Quick Revision

-   String = sequence of characters.
-   Index starts at 0.
-   Negative index starts at -1.
-   Strings are immutable.
-   `[::-1]` reverses a string.
-   Python uses Unicode.
