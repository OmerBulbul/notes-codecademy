# File Input/Output

Now that you understand Python syntax and have been introduced to some Python best practices, let's apply what you've learned to a real-world application: writing data to a file.

## Table of Contents
1. [See It to Believe It](#toc1)
2. [The open() Function](#toc2)
3. [Writing](#toc3)
4. [Reading](#toc4)
5. [Reading Between the Lines](#toc5)
6. [PSA: Buffering Data](#toc6)
7. [The 'with' and 'as' Keywords](#toc7)
8. [Try It Yourself](#toc8)
9. [Case Closed?](#toc9)

<div id='toc1'/>
## See It to Believe It (1/9)
Until now, the Python code you've been writing comes from one source and only goes to one place: you type it in at the keyboard and its results are displayed in the console. But what if you want to read information from a file on your computer, and/or write that information to another file?

This process is called **file I/O** (the "I/O" stands for "input/output"), and Python has a number of built-in functions that handle this for you.

Check out the code in the editor to the right. Note that you now have an extra `output.txt` tab, which is just an empty text file. That's all about to change!

### Instructions
Click Save & Submit Code, then check out the `output.txt` tab to see Python's file I/O powers in action.

<div id='toc2'/>
## The open() Function (2/9)
Let's walk through the process of writing to a file one step at a time.

The first code that you saw executed in the previous exercise was this:

```python
f = open("output.txt", "w")
```

This told Python to open `output.txt` in `"w"` mode ("w" stands for "write"). We stored the result of this operation in a file object, `f`.

Doing this opens the file in write-mode and prepares Python to send data into the file.

### Instructions
Create a variable, `my_file`, and set it equal to calling the `open()` function on `output.txt`. In this case, pass `"r+"` as a second argument to the function so the file will allow you to read *and* write to it! (See the Hint for details.)

###### Hint
You can open files in write-only mode (`"w"`), read-only mode (`"r"`), read and write mode (`"r+"`), and append mode (`"a"`, which adds any new data you write to the file to the end of the file).

<div id='toc3'/>
## Writing (3/9)
Good work! Now it's time to write some data to our `output.txt` file.

We've added the list comprehension from the first exercise to the code in the editor. Our goal in this exercise will be to write each element of that list to `output.txt` (shown in a new tab above the editor) with each number on its own line.

We can write to a Python file like so:

```python
my_file.write("Data to be written")
```

The `write()` function takes a string argument, so we'll need to do a few things here:

You **must** close the file. You do this simply by calling `my_file.close()` (we did this for you in the last exercise). If you don't close your file, Python *won't* write to it properly. From here on out, you gotta close your files!

### Instructions
1. Iterate over `my_list` to get each value
2. Use `my_file.write()` to write each value to `output.txt`
3. Make sure to call `str()` on the iterating data so `.write()` will accept it
4. Make sure to add a newline (`"\n"`) after each element to ensure each will appear on its own line.
5. Use `my_file.close()` to close the file when you're done.

###### Hint
Remember, the syntax for iterating over a list looks like this:

```python
for item in list:
    # Do something
```

You should write to the file inside your iterator, but you should close the file *outside* your iterator -- otherwise, you'll attempt to close the file after you write each line!

And the syntax for calling `str()` looks like this:

```python
str(42)
# => "42"
```

<div id='toc4'/>
## Reading (4/9)
Excellent! You're a pro.

Finally, we want to know how to read from our `output.txt` file. As you might expect, we do this with the `read()` function, like so:

```python
print my_file.read()
```

### Instructions
1. Declare a variable, `my_file`, and set it equal to the file object returned by calling `open()` with both `"output.txt"` and `"r"`.
2. Next, `print` the result of using `.read()` on `my_file`, like the example above.
3. Make sure to `.close()` your file when you're done with it! All kinds of doom will happen if you don't.

###### Hint
Remember, the syntax for opening a file looks like this:

```python
variable = open("filename", "mode")
```

<div id='toc5'/>
## Reading Between the Lines (5/9)
What if we want to read from a file line by line, rather than pulling the entire file in at once. Thankfully, Python includes a `readline()` function that does exactly that.

If you open a file and call `.readline()` on the file object, you'll get the first line of the file; subsequent calls to `.readline()` will return successive lines.

### Instructions
1. Declare a new variable `my_file` and store the result of calling `open()` on the `"text.txt"` file in `"r"`ead-only mode.
2. On three separate lines, `print` out the result of calling `my_file.readline()`. See how it gets the next line each time?
3. Don't forget to `close()` your file when you're done with it!)

###### Hint
Remember, to open a file:

```python
variable = open("filename", "mode")
```

To read from the file, you can just call `variable.readline()`. Make sure to close your file once you're done reading from it!

<div id='toc6'/>
## PSA: Buffering Data (6/9)
We keep telling you that you *always* need to close your files after you're done writing to them. Here's why!

During the I/O process, data is **buffered**: this means that it is held in a temporary location before being written to the file.

Python doesn't **flush the buffer** -- that is, write data to the file -- until it's sure you're done writing. One way to do this is to close the file. If you write to a file without closing, the data won't make it to the target file.

### Instructions
Check out our *extremely bad code* in the editor. Click Save & Submit Code -- you'll note that our `read_file.read()` didn't read any data back! (The text still appears in `text.txt`, though, because we closed the file behind the scenes for you. Safety first!)

1. Add a `write_file.close()` call on line 9.
2. Add a `read_file.close()` on line 13.
3. Run the code again.
4. This time, you'll see the data come through!

<div id='toc7'/>
## The 'with' and 'as' Keywords (7/9)
Programming is all about getting the computer to do the work. Is there a way to get Python to automatically close our files for us?

Of course there is. This is Python.

You may not know this, but file objects contain a special pair of built-in methods: `__enter__()` and `__exit__()`. The details aren't important, but what *is* important is that when a file object's `__exit__()` method is invoked, it automatically closes the file. How do we invoke this method? With `with` and `as`.

The syntax looks like this:

```python
with open("file", "mode") as variable:
    # Read or write to the file
```

### Instructions
Check out the example in the editor. Note that we don't explicitly `close()` our file, and remember that if we don't close a file, our data will get stuck in the buffer. Click Save & Submit Code and check out `text.txt` to see the results.

<div id='toc8'/>
## Try It Yourself (8/9)
It worked! Our Python program successfully wrote to `text.txt`.

### Instructions
Now you try: write any data you like to the `text.txt` file using `with`...`as`. Give your file object the usual name: `my_file`.

###### Hint
Remember your syntax:

```python
with open("file","mode") as variable:
    # Read or write to the file
```

<div id='toc9'/>
## Case Closed? (9/9)
Finally, we'll want a way to test whether a file we've opened is closed. Sometimes we'll have a lot of file objects open, and if we're not careful, they won't all be closed. How can we test this?

```python
f = open("bg.txt")
f.closed
# False
f.close()
f.closed
# True
```

Python file objects have a `closed` attribute which is `True` when the file is closed and `False` otherwise.

By checking `file_object.closed`, we'll know whether our file is closed and can call `close()` on it if it's still open.

### Instructions
Below your `with`...`as` code, do two things:

1. Check `if` the file is not `.closed`.
2. If that's the case, call `.close()` on it.
3. (You don't need an `else` here, since your `if` statement should do nothing if `.closed` is True.)
4. After your `if` statement, `print` out the value of `my_file.closed` to make sure your file is really closed.

###### Hint
Remember, `if` statements look like this:

```python
if expression:
    # Do something
```