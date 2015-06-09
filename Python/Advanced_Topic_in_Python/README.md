# Advanced Topic in Python

## List Slicing Syntax (7/18)
Sometimes we only want part of a Python list. Maybe we only want the first few elements; maybe we only want the last few. Maybe we want every other element!

List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

```python
[start:end:stride]
```

Where `start` describes where the slice starts (inclusive), `end` is where it ends (exclusive), and `stride` describes the space between items in the sliced list. For example, a stride of `2` would select every other item from the original list to place in the sliced list.

### Instructions
We've generated a list with a list comprehension in the editor to the right, and we're about to print a selection from the list using list slicing. Can you guess what will be printed out? Click Save & Submit Code when you think you know!

## Omitting Indices (8/18)
If you don't pass a particular index to the list slice, Python will pick a default.

```python
to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']
```

1. The default starting index is `0`.
2. The default ending index is the end of the list.
3. The default stride is `1`.

### Instructions
1. Use list slicing to `print` out every odd element of `my_list` from start to finish.
2. Omit the start and end index. You only need to specify a `stride`.
3. Check the Hint if you need help.

###### Hint
Remember, the syntax for list slicing is

```python
[start:end:stride]
```

Since you're using the entire list, you should leave out the `start` and `end` indices (but leave in the colons!) and give the slice a `stride` that will select every other (that is, odd) element.

## Reversing a List (9/18)
We have seen that a positive stride progresses through the list from left to right.

A _negative_ stride progresses through the list from right to left.

```python
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
```

In the example above, we print out `['E', 'D', 'C', 'B', 'A']`.

### Instructions
1. Create a variable called `backwards` and set it equal to the reversed version of `my_list`.
2. Make sure to reverse the list in the editor by passing your list slice a negative stride, like in the example above.

## Stride Length (10/18)
A positive stride length traverses the list from left to right, and a negative one traverses the list from right to left.

Further, a stride length of 1 traverses the list "by ones," a stride length of 2 traverses the list "by twos," and so on.

### Instructions
Create a variable, `backwards_by_tens`, and set it equal to the result of going backwards through `to_one_hundred` by tens. Go ahead and print `backwards_by_tens` to the console.

###### Hint
Remember, the syntax is:

```python
new_list = old_list[begin:end:stride]
```

## Practice Makes Perfect (11/18)
Great work! See? This list slicing business is pretty straightforward.

Let's do one more, just to prove you really know your stuff.

### Instructions
1. Create a list, `to_21`, that's just the numbers from 1 to 21, inclusive.
2. Create a second list, `odds`, that contains only the odd numbers in the `to_21` list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.
3. Finally, create a third list, `middle_third`, that's equal to the middle third of `to_21`, from 8 to 14, inclusive.

## Anonymous Functions (12/18)
One of the more powerful aspects of Python is that it allows for a style of programming called *functional programming*, which means that you're allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!

Check out the code at the right. See the `lambda` bit? Typing

```python
lamba x: x % 3 == 0
```

Is the same as

```python
def by_three(x):
    return x % 3 == 0
```

Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an **anonymous function**.

When we pass the lambda to `filter`, `filter` uses the lambda to determine what to filter, and the second argument (`my_list`, which is just the numbers 0 – 15) is the list it does the filtering on.

### Instructions
Can you guess what the this code will `print` to the console? Click Save & Submit Code to see.

## Lambda Syntax (13/18)
Lambda functions are defined using the following syntax:

```python
my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
```

Lambdas are useful when you need a quick function to do some work for you.

If you plan on creating a function you'll use over and over, you're better off using `def` and giving that function a name.

### Instructions
1. Fill in the first part of the `filter` function with a `lambda`. The `lambda` should ensure that only `"Python"` is returned by the `filter`.
2. Fill in the second part of the `filter` function with `languages`, the list to filter.

###### Hint
Remember, `filter()` takes two arguments: the first is the function that tells it what to filter, and the second is the object to perform the filtering on.

## Try It! (14/18)
All right! Time to test out `filter()` and `lambda` expressions.

```python
cubes = [x**3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)
```

The example above is just a reminder of the syntax.

### Instructions
1. Create a list, `squares`, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!
2. Use `filter()` and a `lambda` expression to `print` out only the squares that are between 30 and 70 (inclusive).

###### Hint
You'll want to filter for `x >=30 and x <=70`.

## Iterating Over Dictionaries (15/18)
First, let's review iterating over a `dict`.

### Instructions
Call the appropriate method on `movies` such that it will `print` out all the _items_ (hint, hint) in the dictionary—that is, each key and each value.

###### Hint
You'll just want to `print` the result of calling the `.items()` method on your `movies`. No loops necessary!

## Comprehending Comprehensions (16/18)
Good! Now let's take another look at list comprehensions.

```python
squares = [x**2 for x in range(5)]
```

### Instructions
Use a list comprehension to create a list, `threes_and_fives`, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.

###### Hint
Remember, list comprehension syntax looks like this:

```python
list_name = [var for var in range]
```

You can include an optional `if` statement after the range. (You'll need such an `if` statement to check whether the numbers are evenly divisible by 3 or 5.)

Remember, modulo (`%`) is a good way to check if a number is evenly divisible by another.

## List Slicing (17/18)
Great! Next up: list slicing.

```python
str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
str[start:end:stride]
```

You can think of a Python string as a list of characters.

### Instructions
The string in the editor is garbled in two ways:

1. First, our message is backwards;
2. Second, the letter we want is every other letter.
3. Use list slicing to extract the message and save it to a variable called `message`.

It's important to remember that lists are mutable (changeable) in Python, but strings aren't; when you slice a string, you get back a _new string_. The original string is unchanged unless you purposely "save over" it, like this:

```python
my_string = "Monty Python"
# => Monty Python
my_string = my_string[:-7]
# => Monty
```

## Lambda Expressions (18/18)
Last but not least, let's look over some `lambdas`.

```python
my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
```

We've given you another (slightly different) `garbled`. Sort it out with a `filter()` and a `lambda`.

### Instructions
1. Create a new variable called `message`.
2. Set it to the result of calling `filter()` with the appropriate `lambda` that will filter out the `"X"`s. The second argument will be `garbled`.
3. Finally, `print` your `message` to the console.

###### Hint
Remember, a lambda expression looks like this:

```python
lambda variable: variable expression
```

For example, you might have

lamba x: x != 10

Remember, `filter()` takes two arguments: the first is the function that tells it what to filter (in this case, your lambda expression), and the second is the object to perform the filtering on (the `garbled` string).
