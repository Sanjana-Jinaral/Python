# Day 6 Revision Notes -- Input & Output

## Input

-   Data given to a program.
-   `input()` always returns a `str`.

Example:

``` python
name = input("Enter your name: ")
```

## Output

-   Information displayed by a program.
-   `print()` is used for output.

Example:

``` python
print("Hello")
```

## Internal Working

-   `print()`: Object → print() → stdout → OS → Screen
-   `input()`: Keyboard → OS → stdin → Python → String → Variable

## Type Conversion

``` python
age = int(input())
price = float(input())
```

## f-Strings

``` python
name = "Sanjana"
print(f"Hello {name}")
```

## Escape Characters

-   `\n` New line
-   `\t` Tab
-   `\\` Backslash
-   `\"` Double quote

## print() Parameters

### sep

``` python
print("A","B",sep="-")
```

### end

``` python
print("Hello", end=" ")
print("World")
```

## Interview Questions

1.  What is input?
2.  What is output?
3.  Why does input() return a string?
4.  What is stdin?
5.  What is stdout?
6.  Difference between sep and end?
7.  What are f-strings?
8.  Explain print() internally.
9.  Explain input() internally.
10. Why use type conversion?

## Quick Revision

-   input() → returns str
-   print() → output
-   stdin → Standard Input
-   stdout → Standard Output
-   sep → separator
-   end → replaces newline
-   int(), float() → type conversion
-   f-strings → readable formatting
