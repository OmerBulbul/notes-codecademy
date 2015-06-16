# Introduction to Classes

Classes are a crucial part of object-oriented programming (OOP). In this course, we'll explain what classes are, why they're important, and how to use them effectively.

## Why Use Classes? (1/18)
Python is an object-oriented programming language, which means it manipulates programming constructs called **objects**. You can think of an object as a single data structure that contains data as well as functions; functions of objects are called **methods**. For example, any time you call

```python
len("Eric")
```

Python is checking to see whether the string object you passed it has a length, and if it does, it returns the value associated with that **attribute**. When you call

```python
my_dict.items()
```

Python checks to see if `my_dict` has an `items()` method (which all dictionaries have) and executes that method if it finds it.

But what makes `"Eric"` a string and `my_dict` a dictionary? The fact that they're instances of the `str` and `dict` classes, respectively. A class is just a way of organizing and producing objects with similar attributes and methods.

### Instructions
Check out the code in the editor to the right. We've defined our own class, `Fruit`, and created a `lemon` instance.

When you're ready, click Save & Submit Code to get started creating classes and objects of your own.

## Class Syntax (2/18)
A basic class consists only of the `class` keyword, the name of the class, and the class from which the new class **inherits** in parentheses. (We'll get to inheritance soon.) For now, our classes will inherit from the `object` class, like so:

```python
class NewClass(object):
    # Class magic here
```

This gives them the powers and abilities of a Python object. By convention, user-defined Python class names start with a capital letter.

### Instructions
Create a class called `Animal` in the editor. For now, in the body of your class, use the `pass` keyword. (`pass` doesn't do anything, but it's useful as a placeholder in areas of your code where Python expects an expression.)

###### Hint
Use the example in the instructions as a guide!

## Classier Classes (3/18)
We'd like our classes to do more than... well, nothing, so we'll have to replace our `pass` with something else.

You may have noticed in our example back in the first exercise that we started our class definition off with an odd-looking function: `__init__()`. This function is required for classes, and it's used to **initialize** the objects it creates.  
`__init__()` always takes at least one argument, `self`, that refers to the object being created. You can think of `__init__()` as the function that "boots up" each object the class creates.

### Instructions
Remove the `pass` statement in your `class` definition, then go ahead and `def`ine an `__init__()` function for your `Animal` class. Pass it the argument `self` for now; we'll explain how this works in greater detail in the next section. Finally, put the `pass` into the body of the `__init__()` definition, since it will expect an indented block.

Hint
Your `__init__()` function should look something like this:

```python
def __init__(self):
    pass
```

## Let's Not Get Too Selfish (4/18)
Excellent! Let's make one more tweak to our class definition, then go ahead and **instantiate** (create) our first object.

So far, `__init__()` only takes one parameter: `self`. This is a Python convention; there's nothing magic about the word `self`. However, it's overwhelmingly common to use `self` as the first parameter in `__init__()`, so you should do this so that other people will understand your code.

The part that *is* magic is the fact that `self` is the *first* parameter passed to `__init__()`. Python will use the first parameter that `__init__()` receives to refer to the object being created; this is why it's often called `self`, since this parameter gives the object being created its identity.

### Instructions
Let's do two things in the editor:

1. Pass `__init__()` a second parameter, `name`.
2. In the body of `__init__()`, let the function know that `name` refers to the created object's name by typing `self.name = name`. (This will become crystal clear in the next section.)

###### Hint

Your syntax should look like this:

```python
class Animal(object):
    def __init__(self, name):
        # Set the name parameter here!
```

## Instantiating Your First Object (5/18)
Perfect! Now we're ready to start creating objects.

We can access attributes of our objects using **dot notation** Here's how it works:

```python
class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print my_shape.sides
```

1. First we create a class named `Square` with an attribute `sides`.
2. Outside the class definition, we create a new instance of `Square` named `my_shape` and access that attribute using `my_shape.sides`.

### Instructions
1. Outside the `Animal` class definition, create a variable named `zebra` and set it equal to `Animal("Jeffrey")`.
2. Then `print` out `zebra`'s name.

Click "Stuck? Get a hint!" for an example.

###### Hint
You can create a new `Animal` object named "`Jeffrey`" like this:

```python
zebra = Animal("Jeffrey")
```

You can print out `"Jeffrey"`'s name like this:

```python
print zebra.name
```

## More on __init__() and self (6/18)
Now that you're starting to understand how classes and objects work, it's worth delving a bit more into `__init__()` and `self`. They can be confusing!

As mentioned, you can think of `__init__()` as the method that "boots up" a class' instance object: the `init` bit is short for "initialize."

The first argument `__init__()` gets is used to refer to the instance object, and by convention, that argument is called `self`. If you add additional arguments—for instance, a `name` and `age` for your animal—setting each of those equal to `self.name` and `self.age` in the body of `__init__()` will make it so that when you create an instance object of your `Animal` class, you need to give each instance a name and an age, and those will be associated with the particular instance you create.

### Instructions
Check out the examples in the editor. See how `__init__()` "boots up" each object to expect a name and an age, then uses `self.name` and `self.age` to assign those names and ages to each object? Add a third attribute, `is_hungry` to `__init__()`, and click Save & Submit Code to see the results.

Hint
Your code should look something like this:

```python
def __init__(self, name, age, is_hungry)
    self.name = name
    self.age = age
    self.is_hungry = is_hungry
```

## Class Scope (7/18)
Another important aspect of Python classes is **scope**. The scope of a variable is the context in which it's visible to the program.

It may surprise you to learn that not all variables are accessible to all parts of a Python program at all times. When dealing with classes, you can have variables that are available everywhere (**global variables**), variables that are only available to members of a certain class (**member variables**), and variables that are only available to particular instances of a class (**instance variables**).

The same goes for functions: some are available everywhere, some are only available to members of a certain class, and still others are only available to particular instance objects.

### Instructions
Check out the code in the editor. Note that each individual animal gets its own `name` and `age` (since they're all initialized individually), but they all have access to the member variable `is_alive`, since they're all members of the `Animal` class. Click Save & Submit Code to see the output!

## A Methodical Approach (8/18)
When a class has its own functions, those functions are called **methods**. You've already seen one such method: `__init__()`. But you can also define your own methods!

### Instructions
Add a method, `description`, to your `Animal` class. Using two separate `print` statements, it should print out the `name` and `age` of the animal it's called on. Then, create an instance of `Animal`, `hippo` (with whatever name and age you like), and call its `description` method.

###### Hint
Remember to pass `self` as an argument to `description`. Otherwise, printing `self.name` and `self.age` won't work, since Python won't know which `self` (that is, which object) you're talking about!

Your method should look something like this:

```python
def description(self):
    print self.name
    print self.age
```

After that, all you need to do is create a `hippo` and call its description method with `hippo.description()`!

## They're Multiplying! (9/18)
A class can have any number of **member variables**. These are variables that are available to all members of a class.

```python
hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive
print cat.is_alive
```

1. In the example above, we create two instances of an `Animal`.
2. Then we print out `True`, the default value stored in hippo's `is_alive` member variable.
3. Next, we set that to False and print it out to make sure.
4. Finally, we print out `True`, the value stored in cat's `is_alive` member variable. We only changed the variable in hippo, not in cat.
Let's add another member variable to `Animal`.

### Instructions
1. After line 3, add a second member variable called `health` that contains the string `"good"`.
2. Then, create two new `Animals`: `sloth` and `ocelot`. (Give them whatever names and ages you like.)
3. Finally, on three separate lines, `print` out the `health` of your `hippo`, `sloth`, and `ocelot`.

###### Hint
You can add your member variable right under `is_alive`, like so:

```python
is_alive = True
health   = "good"
```

You can print out your `hippo`'s health with

```python
print hippo.health
```

## It's Not All Animals and Fruits (10/18)
Classes like `Animal` and `Fruit` make it easy to understand the concepts of classes and instances, but you probably won't see many zebras or lemons in real-world programs.

However, classes and objects are often used to model real-world objects. The code in the editor is a more realistic demonstration of the kind of classes and objects you might find in commercial software. Here we have a basic `ShoppingCart` class for creating shopping cart objects for website customers; though basic, it's similar to what you'd see in a real program.

### Instructions
Create an instance of `ShoppingCart` called `my_cart`. Initialize it with any values you like, then use the `add_item` method to add an item to your cart.

###### Hint
Since the `ShoppingCart` class has an `__init__()` method that takes a customer name, I'd create my cart like so:

```python
my_cart = ShoppingCart("Eric")
```

Calling the add_item() method might then be:

```python
my_cart.add_item("Ukelele", 10)
```

## Warning: Here Be Dragons (11/18)
**Inheritance** is a tricky concept, so let's go through it step by step.

Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an **is-a** relationship. For example, a Panda **is a** bear, so a Panda class could inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class (even if they have a lot of attributes and methods in common). Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.

### Instructions
Check out the code in the editor. We've defined a class, `Customer`, as well as a `ReturningCustomer` class that inherits from `Customer`. Note that we don't define the `display_cart` method in the body of `ReturningCustomer`, but it will still have access to that method via inheritance. Click Save & Submit Code to see for yourself!

## Inheritance Syntax (12/18)
In Python, inheritance works like this:

```python
class DerivedClass(BaseClass):
    # code goes here
```

where `DerivedClass` is the new class you're making and `BaseClass` is the class from which that new class inherits.

### Instructions
On lines 1-4, we've created a class named `Shape`.

1. Create your own class, `Triangle`, that inherits from `Shape`, like this:

	```python
class Triangle(Shape):
    # code goes here
```

2. Inside the `Triangle` class, write an `__init__()` function that takes four arguments: `self`, `side1`, `side2`, and `side3`.

3. Inside the `__init__()` function, set `self.side1 = side1`, `self.side2 = side2`, and `self.side3 = side3`.

Click "Stuck? Get a hint!" for an example.

###### Hint
Your code should look something like this:

```python
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
       self.side1 = side1
       self.side2 = side2
       self.side3 = side3
```

## Override! (13/18)
Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent, but to **override** one or more of them.

```python
class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello, %s" % other.name

class CEO(Employee):
    def greet(self, other):
        print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
```

Rather than have a separate `greet_underling` method for our CEO, we **override** (or re-create) the `greet` method on top of the base `Employee.greet` method. This way, we don't need to know what type of Employee we have before we greet another Employee.

### Instructions
1. Create a new class, `PartTimeEmployee`, that inherits from `Employee`.
2. Give your derived class a `calculate_wage` method that overrides `Employee`'s. It should take self and `hours` as arguments.
3. Because `PartTimeEmployee.calculate_wage` overrides `Employee.calculate_wage`, it still needs to set `self.hours = hours`.
4. It should `return` the part-time employee's number of `hours` worked multiplied by `12.00` (that is, they get $12.00 per hour instead of $20.00).

###### Hint
In the example code above, we created an overriding `CEO.greet` method. It had the same arguments as `Employee.greet`. You'll want to add a `calculate_wage()` method to your `PartTimeEmployee` class, and it should also take `self` and `hours` as arguments. Instead of returning `hours * 20.00`, though, it should return `hours * 12.00`.

## This Looks Like a Job For... (14/18)
On the flip side, sometimes you'll be working with a derived class (or **subclass**) and realize that you've overwritten a method or attribute defined in that class' base class (also called a **parent** or **superclass**) that you actually need. Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in `super` call.

The syntax looks like this:

```python
class Derived(Base):
   def m(self):
       return super(Derived, self).m()
```

Where `m()` is a method from the base class.

### Instructions
First, inside your `PartTimeEmployee` class:

1. Add a new method called `full_time_wage` with the arguments `self` and `hours`.
2. That method should `return` the result of a `super` call to the `calculate_wage` method of `PartTimeEmployee`'s parent class. Use the example above for help.

Then, after your class:

1. Create an instance of the `PartTimeEmployee` class called `milton`. Don't forget to give it a name.
2. Finally, `print` out the result of calling his `full_time_wage` method. You should see his wage printed out at $20.00 per hour! (That is, for `10` hours, the result should be `200.00`.)

###### Hint
You super call should look something like this:

```python
def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).method(args)
```

Where `method` is the method you want (`calculate_wage`) and `args` are the arguments that method takes.

## Class Basics (15/18)
First things first: let's create a class to work with.

### Instructions
Create a class, `Triangle`. Its `__init__()` method should take `self`, `angle1`, `angle2`, and `angle3` as arguments. Make sure to set these appropriately in the body of the `__init__()` method (see the Hint for more).

###### Hint
Make sure your `Triangle` inherits from `object`. Remember, class syntax looks like this:

```python
class ClassName(object):
    def __init__(args):
        # Set self.args = args
```

## Class It Up (16/18)
Great! Now let's add a member variable and a method to our class.

### Instructions
Inside the `Triangle` class:

1. Create a variable named `number_of_sides` and set it equal to `3`.
2. Create a method named `check_angles`. The sum of a triangle's three angles should return `True` if the sum of `self.angle1`, `self.angle2`, and `self.angle3` is equal `180`, and `False` otherwise.

###### Hint
The `check_angles` method should look something like this:

```python
def check_angles(self):
  if self.angle1+self.angle2+self.angle3==180:
    return True
  else:
    return False
```

## Instantiate an Object (17/18)
Let's go ahead and create an instance of our `Triangle` class.

### Instructions
1. Create a variable named `my_triangle` and set it equal to a new instance of your `Triangle` class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
2. Print out `my_triangle.number_of_sides`
3. Print out `my_triangle.check_angles()`

###### Hint
Remember, we can instantiate an object like so:

```python
instance = Class(args)
```

Where `args` are the arguments `__init__()` takes, not including `self`.

## Inheritance (18/18)
Finally, let's create an `Equilateral` class that inherits from our `Triangle` class. (An equilateral triangle is a triangle whose angles are all 60˚, which also means that its three sides are equal in length.)

### Instructions
1. Create a class named `Equilateral` that inherits from `Triangle`.
2. Inside `Equilateral`, create a member variable named `angle` and set it equal to `60`.
3. Create an `__init__()` function with only the parameter `self`, and set `self.angle1`, `self.angle2`, and `self.angle3` equal to `self.angle` (since an equilateral triangle's angles will always be 60˚).

###### Hint
Remember, inheritance looks like this:

```python
class DerivedClass(BaseClass):
    # Your code here
```

where `DerivedClass` is the new class you're making, and `BaseClass` is the class it inherits from.