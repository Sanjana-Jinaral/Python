# Day 8 Revision Notes -- String Methods

## String Methods

String methods operate on string objects. Since strings are immutable,
methods return new strings.

## Case Methods

-   upper()
-   lower()
-   title()
-   capitalize()
-   swapcase()

## Search Methods

-   find() -\> returns index or -1
-   index() -\> returns index or ValueError

## Count

``` python
"banana".count("a")
```

## Replace

``` python
text.replace("Java","Python")
```

## Split & Join

-   split() -\> string to list
-   join() -\> list to string

## Whitespace

-   strip()
-   lstrip()
-   rstrip()

## Validation

-   isalpha()
-   isdigit()
-   isalnum()
-   isspace()
-   startswith()
-   endswith()

## Important

Methods do not modify the original string.

## Interview Questions

1.  What is a string method?
2.  Why are strings immutable?
3.  find() vs index()?
4.  split() vs join()?
5.  Why doesn't upper() modify the original string?
6.  What does strip() do?
7.  What does replace() return?
8.  Why does split() return a list?
9.  What does count() do?
10. Explain startswith() and endswith().

## Quick Revision

-   Strings are immutable.
-   Methods return new strings.
-   find() -\> -1
-   index() -\> ValueError
-   split() -\> list
-   join() -\> string
-   strip() removes spaces.
