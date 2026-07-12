# Day 4A Revision Notes -- How Python Works Internally

## Execution Flow

``` text
Source Code (.py)
↓
Lexer
↓
Tokens
↓
Parser
↓
AST
↓
Compiler
↓
Bytecode (.pyc)
↓
Python Virtual Machine (PVM)
↓
Operating System
↓
CPU
↓
Output
```

## Key Concepts

-   **Source Code:** Human-readable Python code.
-   **(Lexical Analysis)Lexer:** Breaks source code into tokens.
-   **Tokens:** Smallest meaningful units.(small pieces of code)
-   **Parser:** Checks syntax and creates AST.
-   **AST:** Tree representation of the program.(Think of the AST as a map that describes the structure of your code.)
-   **Compiler:** Converts AST into bytecode.
-   **Bytecode:** Intermediate code understood by the PVM.
-   **PVM:** Executes(instruction by instruction) bytecode. (Without the PVM no Python program can run.)
-   **Operating System:** Loads Python and provides hardware resources.
-   **CPU:** Executes machine instructions.

## Important Points

-   CPU cannot understand Python source code.
-   CPython first compiles to bytecode, then executes it using the PVM.
-   Compiled bytecode may be stored in `__pycache__` as `.pyc` files.

# Interview Questions

1.  What is source code?
2.  What is CPython?
3.  What is the Python interpreter?
4.  What is lexical analysis?
5.  What is a token?
6.  What is a parser?
7.  What is an AST?
8.  What is bytecode?
9.  What is the PVM?
10. Is Python compiled or interpreted?
11. Explain Python execution from source code to output.
12. Why can't the CPU execute Python code directly?
13. What is the purpose of the __pycache__ folder?


# Quick Revision

-   Source Code → Lexer → Tokens → Parser → AST → Compiler → Bytecode →
    PVM → OS → CPU → Output


## Questions and Answers

1. Who loads Python into memory?
**ans:** Operating System.

2. What is a Token?
**ans:** A token is the smallest meaningful unit of a program recognized by the Python lexer.

3. Why do we need an AST?
**ans:** - Because it's much easier for Python to optimize and compile a structured tree than raw text.
- The AST is an internal representation of your program.

4. What is Bytecode?
**ans:** Bytecode is an intermediate language. It is a language that the Python Virtual Machine understands.

5. Sometimes Python stores the bytecode in a file like '__pycache__/' Example: hello.cpython-313.pyc' why?
**ans:** Because next time, Python can reuse the compiled bytecode instead of compiling everything again, making startup faster in many cases.


## Complete Flow
``` text
You Write Code (.py)
↓
Operating System Starts Python(It finds the Python interpreter. Then it loads Python into RAM.)
↓
Python Reads Source Code(opens and reads. It is still just text.)
↓
Lexer
↓
Tokens
↓
Parser
↓
AST
↓
Compiler
↓
Bytecode (.pyc)
↓
Python Virtual Machine
↓
Operating System
↓
CPU
↓
Output
```
