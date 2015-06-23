# Python Syntax

This tutorial will introduce you to Python, a general-purpose, object-oriented interpreted language you can use for countless standalone projects or scripting applications.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<div id='top'/>
## Table of Contents

- [Variables and Data Types](#variables-and-data-types)
	- [Welcome! (1/13)](#welcome-113)
	- [Variables (2/13)](#variables-213)
	- [Booleans (3/13)](#booleans-313)
	- [You've Been Reassigned (4/13)](#youve-been-reassigned-413)
- [Whitespace and Statements](#whitespace-and-statements)
	- [Whitespace (5/13)](#whitespace-513)
	- [Whitespace Means Right Space (6/13)](#whitespace-means-right-space-613)
	- [A Matter of Interpretation (7/13)](#a-matter-of-interpretation-713)
- [Comments](#comments)
	- [Single Line Comments (8/13)](#single-line-comments-813)
	- [Multi-Line Comments (9/13)](#multi-line-comments-913)
- [Math Operations](#math-operations)
	- [Math (10/13)](#math-1013)
	- [Exponentiation (11/13)](#exponentiation-1113)
	- [Modulo (12/13)](#modulo-1213)
- [Review](#review)
	- [Bringing It All Together (13/13)](#bringing-it-all-together-1313)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<div id='variables-and-data-types'/>
# Variables and Data Types
<div id='welcome-113'/>
## Welcome! (1/13)
[[Back to Top]](#top)

Python is an easy to learn programming language. You can use it to create web apps, games, even a search engine!

Ready to learn Python? Click Save & Submit Code to continue!

### Instructions
Ready to learn Python? Click Save & Submit Code to continue!

###### Hint
If the loading bar fills but doesn't fade away, try refreshing the page.

<div id='variables-213'/>
## Variables (2/13)
[[Back to Top]](#top)

Creating web apps, games, and search engines all involve storing and working with different types of data. They do so using **variables**. A **variable** stores a piece of data, and gives it a specific name.

For example:

```python
spam = 5
```

The variable `spam` now stores the number `5`.

### Instructions
1. Set the variable `my_variable` equal to the value `10`.
2. Click the Save & Submit button to run your code.

###### Hint
Make sure to put `my_variable` on the left side of the `=`, and `10` on the right.

You will notice that the window says "None" in it when you run the code. This is the "result" of your code, but you can generally ignore it.

<div id='booleans-313'/>
## Booleans (3/13)
[[Back to Top]](#top)

Great! You just stored a number in a variable. Numbers are one data type we use in programming. A second data type is called a **boolean**.

A **boolean** is like a light switch. It can only have two values. Just like a light switch can only be on or off, a boolean can only be `True` or `False`.

You can use variables to store booleans like this:

```python
a = True
b = False
```

### Instructions
Set the following variables to the corresponding values:

1. `my_int` to the value `7`
2. `my_float` to the value `1.23`
3. `my_bool` to the value `True`

###### Hint
Remember to capitalize `True`!

<div id='youve-been-reassigned-413'/>
## You've Been Reassigned (4/13)
[[Back to Top]](#top)

Now you know how to use variables to store values.

Say `my_int = 7`. You can change the value of a variable by "reassigning" it, like this:

```python
my_int = 3
```

### Instructions
Try it and see! Change the value of `my_int` from `7` to `3` in the editor

###### Hint
All you need to do is type `3` after the equals sign on line 8.

<div id='whitespace-and-statements'/>
# Whitespace and Statements
<div id='whitespace-513'/>
## Whitespace (5/13)
[[Back to Top]](#top)

In Python, whitespace is used to structure code. Whitespace is important, so you have to be careful with how you use it.

### Instructions
The code on the right is badly formatted. Hit "Save & Submit Code" to see what happens.

You should see an error message. We'll fix it in the next exercise!

<div id='whitespace-means-right-space-613'/>
## Whitespace Means Right Space (6/13)
[[Back to Top]](#top)

Now let's examine the error from the last lesson:

```python
IndentationError: expected an indented block
```

You'll get this error whenever your whitespace is off.

### Instructions
Properly indent the code with four spaces before eggs on line 2 and another four before return on line 3.

You should indent your code with four spaces.

###### Hint
Your code should look something like this:

```python
def spam():
    eggs = 12
    return eggs

print spam()
```
<div id='a-matter-of-interpretation-713'/>
## A Matter of Interpretation (7/13)
[[Back to Top]](#top)

The window in the top right corner of the page is called the interpreter. The interpreter runs your code line by line, and checks for any errors.

```python
cats = 3
```

In the above example, we create a variable `cats` and assign it the value of `3`.

### Instructions
1. Create a variable called `spam` and assign it the value of `True`.
2. Create a variable called `eggs` and assign it the value of `False`.

###### Hint
Remember, you assign values with the `=` sign, like so:

```python
example_variable = True
```

<div id='comments'/>
# Comments
<div id='single-line-comments-813'/>
## Single Line Comments (8/13)
[[Back to Top]](#top)

You probably saw us use the `#` sign a few times in earlier exercises. The `#` sign is for comments. A comment is a line of text that Python won't try to run as code. It's just for humans to read.

Comments make your program easier to understand. When you look back at your code or others want to collaborate with you, they can read your comments and easily figure out what your code does.

### Instructions
Write a comment on line 1. Make sure it starts with `#`. It can say anything you like.

###### Hint
You comment could be something like this:

```python
# What is the value of mysterious_variable?
```

Note that if you delete `mysterious_variable`, you may see an error in the console. You can ignore it.

<div id='multi-line-comments-913'/>
## Multi-Line Comments (9/13)
[[Back to Top]](#top)

The `#` sign will only comment out a single line. While you could write a multi-line comment, starting each line with `#`, that can be a pain.

Instead, for multi-line comments, you can include the whole block in a set of triple quotation marks:

```python
"""Sipping from your cup 'til it runneth over,
Holy Grail.
"""
```

### Instructions
Write a multi-line comment in the editor. It can be any text you'd like!

###### Hint
Your multiline comment is just a regular phrase or sentence starting with `"""` and ending with `"""`. No `#` needed at all!

<div id='math-operations'/>
# Math Operations
<div id='math-1013'/>
## Math (10/13)
[[Back to Top]](#top)

Great! Now let's do some math. You can add, subtract, multiply, divide numbers like this

```
addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9
```

### Instructions
Set the variable `count_to equal` to the sum of two big numbers.

###### Hint
Remember, you can set a variable equal to a value with

```python
variable_name = # Add your value here!
```
<div id='exponentiation-1113'/>
## Exponentiation (11/13)
[[Back to Top]](#top)

All that math can be done on a calculator, so why use Python? Because you can combine math with other data types (e.g. **booleans**) and commands to create useful programs. Calculators just stick to numbers.

Now let's work with exponents.

```python
eight = 2 ** 3
```

In the above example, we create a new variable called `eight` and set it to `8`, or the result of 2 to the power to 3 (2^3).

Notice that we use `**` instead of `*` or the multiplication operator.

### Instructions
Create a new variable called `eggs` and use exponents to set `eggs` equal 100.

Try raising 10 to the power of 2.

<div id='modulo-1213'/>
## Modulo (12/13)
[[Back to Top]](#top)

Our final operator is **modulo**. **Modulo** returns the remainder from a division. So, if you type `3 % 2`, it will return `1`, because 2 goes into 3 evenly once, with 1 left over.

### Instructions
Use modulo to set `spam` equal to `1`. You can use any two numbers that will leave a remainder of `1` to do this.

###### Hint
Any odd number `% 2` will equal 1 (since dividing any odd number by 2 always leaves 1 as a remainder).

Remember that you can't divide by 0 or you will get an error. Same goes for `%`. `10 % 0` will cause an error!

<div id='review'/>
# Review
<div id='bringing-it-all-together-1313'/>
## Bringing It All Together (13/13)
[[Back to Top]](#top)

Nice work! So far, you've learned about:

- **Variables**, which store values for later use
- **Data types**, such as numbers and booleans
- **Whitespace**, which separates statements
- **Comments**, which make your code easier to read
- **Arithmetic operations**, including `+`, `-`, `*`, `/`, `**`, and `%`

### Instructions
Let's put our knowledge to work.

1. Write a single-line comment on line 1. It can be anything! (Make sure it starts with `#`)
2. Set the variable monty equal to `True`.
3. Set another variable `python` equal to `1.234`.
4. Set a third variable `monty_python` equal to `python` squared.

###### Hint
You can use arithmetic operators directly on variables! Remember, `python` squared means `python ** 2`.

Note that the name of the variable `monty_python` has nothing to do with the name of the variables `monty` and `python`. We just decided to use these variable names because Python people love Monty Python's Flying Circus!