## Higher Order Function
A function that either accepts a function as an argument or returns a function as a return value

### Function as input argument
```python
def one():
	return 1

print(type(one))  # returns <class 'function'>
```
```python
def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def calculate(func, a, b):
	return func(a, b)

print(calculate(add, 5, 3))
```

### Nested Functions
They are accessible only to the body of the function they belong to
```python
# Gallons to cups
  
# 1 gallon = 4 quarts
# 1 quart = 2 pints
# 1 pint = 2 cups

def convert_gallons_to_cups(gallons):
	def gallons_to_quarts(gallons):
		print(f"Converting {gallons} gallons to quarts")
		return gallons * 4
		
	def quarts_to_pints(quarts):
		print(f"Converting {quarts} quarts to pints")
		return quarts * 2

	def pints_to_cups(pints):		
		print(f"Converting {pints} pints to cups")
		return pints * 2

	return pints_to_cups(quarts_to_pints(gallons_to_quarts(gallons)))


print(convert_gallons_to_cups(2))
```

### Function as a return argument
```python
def calculator(operation):
	
	def add(a, b):
		return a + b
	
	def subtract(a, b):
		return a - b

	if operation == "add":	
		return add
	elif operation == "subtract":
		return subtract
	
	return operation

print(calculator("add")(5, 3))
print(calculator("subtract")(7, 8))
print(calculator("multiply"))
```

### Functions as object elements
```python
def square(num):
	return num ** 2

def cube(num):
	return num ** 3

def times10(num):
	return num * 10

  
operations = [square, cube, times10]

for func in operations:
	print(func(5))
```

## Scope
Scope is the locations in the program in which a name (variable, function etc.) can be used.
A lower level scope can access a name from a higher level scope but not vice versa.

### Global vs. Local Variables
Global Variable: It is available in the current file
Local Variable: It is available to the scope it is defined

Shallow Variable: A local variable that shares the same name as global variable
```python
age = 28 # global variable

def fancy_function():
	age = 100 # local shallow variable
	print(age)

fancy_function() # 100
print(age) # 28
```

Constant: A name for a value that does not change over the program's execution. Capital letters are used for the constant's names
```python
TAX_RATE = 0.06

def calculate_tax(price):
	return round(price * TAX_RATE, 2)

def calculate_tip(price):
	return round(price * TAX_RATE * 3, 2)
```

### LEGB
Local / Enclosing Functions / Global / Built-in
Python will search for through this sequence of order to find a name. If it does not find the name, it will search in the next scope. If not found, it raises a NameError exception.

### Closure
A programming pattern in which a scope retains access to an enclosing scope's name
```python
def outer():
	candy = "Snickers"

	def inner():	
		return candy
	
	return inner


the_func = outer()
print(the_func())
```

### Global Keyword
Designates that a variable will be global

without global keyword:
```python
x = 10

def change_stuff():
	x = 15

print(x)  # 10
change_stuff()  # prints nothing
print(x)  # 10
```
with global keyword
```python
x = 10

def change_stuff():
	global x
	x = 15

print(x)  # 10
change_stuff()  # prints nothing
print(x)  # 15
```
If x is defined only in the change_stuf() function, it will be accessible only after the function invocation so that the variable has been declared:
```python
# x = 10

def change_stuff():
	global x
	x = 15

# print(x)
#change_stuff()
print(x)  # NameError exception
```

Warning: The usage of global keyword in a local scope is discouraged!!!

### Nonlocal Keyword
Makes a variable accessible/visible to the enclosing function's scope
```python
def outer():
	bubble_tea_flavor = "Black"

	def inner():	
		bubble_tea_flavor = "Green"

	inner()

	return bubble_tea_flavor

print(outer())  # Black
```

```python
def outer():
	bubble_tea_flavor = "Black"

	def inner():
		nonlocal bubble_tea_flavor
		bubble_tea_flavor = "Green"

	inner()

	return bubble_tea_flavor

print(outer())  # Green
```

## Decorators

### Definition
A **decorator** is a higher-order function that _both_ accepts a function as an input and returns another function as an output. It performs some additional operations around the execution of the original function.

### Decorator without arguments
A decorator adds a functionality on top of another function's functionality.
```python
# decorator function
def be_nice(fn):
	def fn_decorated():
		print("Please be nice")
		fn()
		print("Have a nice day")

	return fn_decorated
  
def complex_business_logic():
	print("Something Complex")

complex_business_logic_decorated = be_nice(complex_business_logic)
complex_business_logic_decorated()

# output:
# Please be nice
# Something Complex
# Have a nice day
```
An alternative syntax is using @decorator_function. Whenever the desired function is called, the decorator will be invoked with the desired function as argument:
```python
# decorator function
def be_nice(fn):
	def fn_decorated():
		print("Please be nice")
		fn()
		print("Have a nice day")

	return fn_decorated

@be_nice
def complex_business_logic():
	print("Something Complex")

complex_business_logic() # be_nice(complex_business_logic)()
```
Example:
Decorators can be used to measure the time it takes for a function to complete.

### Decorator with arguments
In the previous example, when *complex_business_logic* is called, the *fn_decorated* is called, which accepts no arguments. So, the following syntax will raise a TypeError:
```python
@be_nice
def complex_business_logic(stakeholder):
	print(f"Something Complex for {stakeholder}")
```
We could pass the *stakeholder* argument to the *fun_decorated* function. But this is not a good solution because we want the decorator to be generic (many functions may use it). To resolve this issue we *args* and *kwargs*:
```python
def be_nice(fn):

	def fn_decorated(*args, **kwargs):
		print("Please be nice")
		fn(*args, **kwargs)
		print("Have a nice day")

	return fn_decorated

@be_nice
def complex_business_logic(stakeholder, position):
	print(f"Something Complex for our {position} {stakeholder}")

complex_business_logic("Boris", position="CEO")
```
The arguments *args* and *kwargs* arguments in the *fn_decorated* are used to pass any number of positional and keyword arguments respectively. On the other hand, the *args* and *kwargs* arguments in the *fn* invocation function are used to unravel/destructure any positional or keyword arguments, respectively.
In fact 
```python
complex_business_logic("Boris", position="CEO")
```
invokes
```python
be_nice(complex_business_logic("Boris", position="CEO"))
```
and *complex_business_logic* is the input for *be_nice*, whereas *("Boris", position="CEO")* is the input for *fn_decorated*
### Return values
Method 1
```python
def be_nice(fn):
	def fn_decorated(*args, **kwargs):
		print("Please be nice")
		result = fn(*args, **kwargs)
		print("Have a nice day")
		return result
	
	return fn_decorated

@be_nice
def complex_business_sum(a, b):
	return a + b

print(complex_business_sum(a=1, b=2))
```
If don't use any decorator for our function, using docstring and the help() function we can print the documentation of our functions
```python
def complex_business_sum(a, b):
	"Adds two numbers together"
	return a + b

help(complex_business_sum)  # prints: Adds two numbers together
```
However, if we use a decorator, the documentation of the *fn_decorated* will be printed, which is undesirable. To preserve the function's documentation, we use a decorator for *fn_decorated*.
Method 2:
```python
import functools

def be_nice(fn):
	@functools.wraps(fn)
	def fn_decorated(*args, **kwargs):
		print("Please be nice")
		result = fn(*args, **kwargs)
		print("Have a nice day")
		return result
		
	return fn_decorated

@be_nice
def complex_business_sum(a, b):
	"Adds two numbers together"
	return a + b

help(complex_business_sum)  # prints: Adds two numbers together 
```