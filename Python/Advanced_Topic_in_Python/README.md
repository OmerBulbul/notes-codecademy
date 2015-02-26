#Advanced Topic in Python

##List Slicing Syntax (7/18)
Sometimes we only want part of a Python list. Maybe we only want the first few elements; maybe we only want the last few. Maybe we want every other element!

List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

```python
[start:end:stride]
```

Where `start` describes where the slice starts (inclusive), `end` is where it ends (exclusive), and `stride` describes the space between items in the sliced list. For example, a stride of `2` would select every other item from the original list to place in the sliced list.

###Instructions
We've generated a list with a list comprehension in the editor to the right, and we're about to print a selection from the list using list slicing. Can you guess what will be printed out? Click Save & Submit Code when you think you know!

##Omitting Indices (8/18)
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

###Instructions
1. Use list slicing to `print` out every odd element of `my_list` from start to finish.
2. Omit the start and end index. You only need to specify a `stride`.
3. Check the Hint if you need help.

######Hint
Remember, the syntax for list slicing is
```python
[start:end:stride]
```
Since you're using the entire list, you should leave out the `start` and `end` indices (but leave in the colons!) and give the slice a `stride` that will select every other (that is, odd) element.

##Reversing a List (9/18)
We have seen that a positive stride progresses through the list from left to right.

A _negative_ stride progresses through the list from right to left.

```python
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
```
In the example above, we print out `['E', 'D', 'C', 'B', 'A']`.

###Instructions
1. Create a variable called `backwards` and set it equal to the reversed version of `my_list`.
2. Make sure to reverse the list in the editor by passing your list slice a negative stride, like in the example above.

##Stride Length (10/18)

A positive stride length traverses the list from left to right, and a negative one traverses the list from right to left.

Further, a stride length of 1 traverses the list "by ones," a stride length of 2 traverses the list "by twos," and so on.

###Instructions
Create a variable, `backwards_by_tens`, and set it equal to the result of going backwards through `to_one_hundred` by tens. Go ahead and print `backwards_by_tens` to the console.

######Hint
Remember, the syntax is:

```python
new_list = old_list[begin:end:stride]
```
