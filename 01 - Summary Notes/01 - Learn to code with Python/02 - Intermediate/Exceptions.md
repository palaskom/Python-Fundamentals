## Definitions
Exception handling is code that handles errors, code that runs when a program does not go as planned.
An exception is an error that occurs during the execution of a program.

An exception is a special object that Python uses to manage errors during program execution.
A traceback is a report of the execution that was raised.

## Catch Exceptions
```python
def divide_five_by_number(n):
	try:
		return 5 / n
	except ZeroDivisionError:
		return "You can't divide by zero!"
	except TypeError as e:
		return f"No dividing by invalid objects! {e}"
```
```python
def divide_five_by_number(n):
	try:
		return 5 / n
	except (ZeroDivisionError, TypeError) as e:
		return f"Something went wrong. The error was {e}"
```
Catching a specific exception is generally better than catching any exception because it leads to clearer, more maintainable, and more reliable code. It improves debugging as specific exceptions help pinpoint the exact problem. So, each problem can be handled accordingly.
## Raise Exceptions
```python
def add_positive_numberss(a, b):
	try:
		if a <=0 or b<=0:
		raise ValueError("One or both of the values is invalid. Both numbers are invalid.")

	return a + b
	except ValueError as e:
	return f"Caught the ValueError: {e}"
```
## Create custom exceptions
```python
class NegativeNumbersError(Exception):
	"""One or more inputs are negative"""
	pass


def add_positive_numbers(a, b):
	try:
		if a <= 0 or b <= 0:
		raise NegativeNumbersError
	except NegativeNumbersError:
		return "Not valid!"
```
When we have multiple error falling in the same category, it is a good practice to create a base exception and all exceptions to fall into that category:
```python
class Mistake(Exception):
	pass

  
class StupidMistake(Mistake):
	pass

  
class SillyMistake(Mistake):
	pass

  
try:
	raise StupidMistake("Extra stupid mistake")
except StupidMistake as e:
	print(f"Caught the error: {e}")

# try:
	# raise StupidMistake("Extra stupid mistake")
# except SillyMistake as e:
	# print("Caught the error: {e}")

try:
	raise StupidMistake("Extra stupid mistake")
except Mistake as e:
	print(f"Caught the error: {e}")
```
## Else-Finally
```python
# x = 10
try:
	print(x + 10)
except NameError:
	print("Some variable is not defined!")
else:
	print("This will print if there is no error in the try.")
finally:
	print("This will print with or without exception")
	print("Closing file...")
```