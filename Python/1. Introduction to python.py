'''



● Familiarization with the basics of Python programming:  Introduction to Python, Features 
of Python, executing a simple “hello world" program, execution modes: interactive mode 
and script mode, Python character set, Python tokens( keyword, identifier, literal, operator, 
punctuator), variables, concept of l-value and r-value, use of comments 

● Knowledge of data types: Number(integer, floating point,complex), boolean, 
sequence(string,  list,  tuple),  None,  Mapping(dictionary),  mutable  and  immutable  data 
types. 

● Operators: arithmetic operators, relational operators, logical operators, assignment 
operators,  augmented  assignment  operators,  identity  operators  (is,  is  not),  membership 
operators (in not in) 

● Expressions,  statement,  type  conversion,  and  input/output:  precedence  of  operators, 
expression, evaluation of an expression, type-conversion (explicit and implicit conversion), 
accepting data as input from the console and displaying output. 

● Errors- syntax errors, logical errors, and run-time errors  

● Flow of Control: introduction, use of indentation, sequential flow, conditional and iterative 
flow 

● Conditional statements: if, if-else, if-elif-else, flowcharts, simple programs:  e.g.: absolute 
value, sort 3 numbers and divisibility of a number. 

● Iterative Statement: for loop, range(), while loop, flowcharts, break and continue 
statements, nested loops, suggested programs: generating pattern, summation of series, 
finding the factorial of a positive number, etc




Guido Ron Vassum in 1991
Monty Python's flying circus
an object oriented programming lang
interpreted
based on ABC and modula-3
adv - easy to use, completness, open source, cross platform, interpreted, expressive
dis adv - not fastest, less libraries, not easily convertible




Tokens or lexical units    (complete meaningfull units)
=============================================================
1. KEYWORDS
    have special meaning
    for, in, print, range

2. LITERALS
    string
        single line
        multi line
    numeric
        integer
            decimal
            octal
            hexadecimal
            bool = 0,1
        float
        long
        complex 
            traditional iota is represented by j

    boolean - True, False
    special literal None
    Literal collections
        list
        tuple
        dict

3. IDENTIFIERS
    name of objects
    such as x is indentifier if 
    x = 5

4. OPERATORS
    arithmetic : + - * / % ** //
    bitwise    : & ^ |
    shift      : << >>
    identity   : is   is not
    relational : < <= > >= == !=
    logical    : and or
    assignment : =
    membership : in not in
    arithmetic-assignment : += -= /= *= %= **= //=

5. PUNCTUATORS
    ()[]{},.:;'"
=============================================================




OPERATOR PRECEDENCE
=============================================================
**                   |      Exponenent
~ + -                |      Complement, unary plus and minus
* / % //             |      Multiply, divide, modulo, floor
+ -                  |      Addition, Subtraction
>> <<                |      Bitwise shift
&                    |      Bitwise AND
^ |                  |      Bitwise XOR and OR
<= < > >=            |      Comparision
<> == !=             |      Equality
= %= /= //= -= +=    |      Arthematic assignment
is is not            |      identitiy
in not in            |      Membership
not or and           |      Logical


* All operators move L to R but exponential moves R to L
* eg :- 2**3**2 = 512, not 64
=============================================================




Datatypes
=============================================================
int      immutable
float    immutable
bool     immutable
str      immutable
list     mutable
tuple    immutable
dict     mutable
=============================================================





TYPECASTING
=============================================================
1. Implicit (automatically by python)
    a = 3.0       # float
    b = 9         # int
    c = a + b     # 12.0 , float

2. Explicit
    a = 3.0       # float
    b = 9         # int
    c = int(a + b)     # 12.0 , int
=============================================================





Loops
=============================================================
for:
else:

    else will be executed when loop runs fully

while:
else:

    else will be executed when loop runs fully i.e. condition becomes false


else wont be executed if loop breaks using break statement
=============================================================





modules
math
    sqrt
    exp
    floor
    log
    log10
    pow
    sin
    cos
    tan
    degrees
    radians
    pi

    etc...etc...


random
    randint(x,y)    
        here x and y are included/inclusive
    randrange(x,y)
        y is exclusive

statistics
    mean
    mode
    median

    etc...etc...




Debugging
Errors
    compile time error
        syntax error
        semantics error
    logical error
    runtime error




FLOW OF CONTROL
=============================================================
1. Conditional Statements
    1.1 if
    1.2 if else
    1.3 if elif else
2. Looping Statements
    2.1 For 
    2.2 While
=============================================================




























'''












