# Day 4B Revision Notes -- Memory, Objects & References

## Memory

-   Python programs run in RAM.
-   The Operating System loads the Python interpreter into RAM.

## Stack vs Heap (Simplified)

-   **Stack:** Holds function information and variable references.
-   **Heap:** Stores Python objects.

## Object

Everything in Python is an object. Every object has: - Identity - Type -
Value

## Reference

Variables do **not** store values. They **refer to objects**.

Example:

``` python
a = 10
b = a
```

One object, two references.

## id()

Returns the identity (unique identifier during an object's lifetime).

## Reference Counting

Python tracks how many references point to an object.

## Garbage Collection

Objects with no remaining references can be cleaned up automatically.

## Small Integer Caching

CPython usually reuses integers from **-5 to 256**.

## String Interning

Python may reuse identical string objects.

# Interview Questions

1.  What is RAM?
2.  What is an object?
3.  What is a reference?
4.  Do variables store values?
5.  What does `id()` return?
6.  What is reference counting?
7.  What is garbage collection?
8.  Explain small integer caching.
9.  Explain string interning.
10. Explain memory for `a = 10; b = a`.

# Quick Revision

-   Variables refer to objects.
-   Heap stores objects.
-   Stack stores references (simplified model).
-   `id()` returns object identity.
-   Python uses reference counting.
-   Garbage collection removes unreachable objects.
