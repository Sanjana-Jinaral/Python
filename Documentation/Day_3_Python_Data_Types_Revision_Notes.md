 Day 3 -- Python Data Types (Short Revision Notes)

## Data

Information that a computer stores and processes.

## Data Type

Specifies what kind of value a variable holds.
Without data types, Python wouldn't know:
- How much memory to use.
- What operations are allowed.

## Built-in Types

-   int
-   float
-   str
-   bool
-   complex

## Collection Types

### List

Ordered, Mutable

### Tuple

Ordered, Immutable

### Set

Unique values, Unordered

### Dictionary

Key-Value pairs

## Mutable

list, set, dictionary
Can be modified.

Examples:

list
dictionary
set

Example:
``` python
fruits = ["Apple"]

fruits.append("Mango")
```

The same list object is updated.

## Immutable

int, float, str, tuple, bool

Cannot be changed after creation.

Examples:

int
float
str
tuple
bool

Example:
``` python
name = "Sanjana"

name = "Priya"
```

Python doesn't modify the old string.

It creates a new string object and name now refers to the new object.

## Type Conversion

``` python
int("22")
float("3.14")
str(100)
bool(1)
```

# Interview Questions

1.  What is data?
2.  What is a data type?
3.  Name Python built-in data types.
4.  Difference between int and float.
5.  What is a string?
6.  Difference between list and tuple.
7.  Difference between set and dictionary.
8.  What is mutable?
9.  What is immutable?
10. Why are strings immutable?
11. What is type conversion?
12. Why does input() return a string?

# Quick Revision

-   Data = Information
-   List = Mutable
-   Tuple = Immutable
-   Set = Unique values
-   Dictionary = Key-Value pairs
