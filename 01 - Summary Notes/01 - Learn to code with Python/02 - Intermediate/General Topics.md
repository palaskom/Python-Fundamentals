# Mutability

In programming, **mutability** refers to whether or not an object can be modified after it has been created. An object is said to be **mutable** if its state or content can be changed, while **immutable** objects cannot be modified once created.
 
1. **Mutable Objects:**
- Examples: Lists, dictionaries, sets in Python.
- You can change their content (e.g., add, remove, or update elements) without creating a new object.
- Example in Python:
 ```python
my_list = [1, 2, 3]
my_list.append(4) # The same list is updated
print(my_list) # Output: [1, 2, 3, 4]
```

2. **Immutable Objects:**
- Examples: Strings, tuples, integers, and floats in Python.
- Any “modification” creates a new object rather than altering the original one.
- Example in Python:
 ```python
my_string = "hello"
new_string = my_string + " world"  # A new string object is created
print(my_string)  # Output: "hello" (original unchanged)
print(new_string)  # Output: "hello world"
```
  
3. **Why does mutability matter?**

- **Performance**: Mutable objects can be more efficient for certain operations since they don’t require creating new objects.
- **Safety**: Immutable objects are safer in multithreading or when used as keys in dictionaries because they cannot change unexpectedly.
- **Semantics**: The choice between mutable and immutable objects depends on the use case and desired behavior.

Understanding the mutability of an object helps in writing better and more predictable code, especially in situations involving data sharing or concurrency.

# Objects & References

## General 

A variable is a name, a reference to an object. In Python variables don't have a type. (A variable is like the address of a house, not the house itself)

Objects have type

In Python we can change the type of object a variable refers to (e.g., a variable x can point to an integer, and then to a list). But it is not a good practise.

## Garbage Collection

Objects that are not referenced by any variable are removed by the Garbage Collector

## Shared References

Immutable objects do not allow for changing their contents. So, if two variable reference it, there is no point of confusion since the object cannot change. 

```python
a = 3
b = a

print(a) # 3
print(b) # 3

a = 5
print(a) # 5
print(b) # 3
```

However, we need to be very careful when it comes to the mutable objects (i.e., lists).

```python
a = [1, 2, 3]
b = a

a.append(4)

print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 3, 4]

b.append(5)

print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]
```

# Equality vs. Identity

## Definition

Equality checks whether two objects are equal, that is, whether they have the same values.

Identity checks if two names in the program point to the actual same object our computer's memory (it's like a house being on a corner and assigned two addresses).

In Python the == operator is used for equality check and the 'is' for identity check:
```python
students = ["Bob", "Sally", "Sue"]
athletes = students
nerds = ["Bob", "Sally", "Sue"]

print(students == athletes) # True
print(students == nerds) # True

print(students is athletes) # True
print(students is nerds) # False
```

Now Python treats immutable types (like the integer, the float, the string and the boolean) differently. It actually doesn't bother creating multiple objects for them in memory.

There's no need for multiple objects to be created because these objects cannot be mutated and there's no risk for multiple names referencing the same object because it can't accidentally be modified.

So, imagine you had a 100 variables referencing the same string of Hello. If you wanted to overwrite the value of one variable to hold an uppercase version of the string, you might call the upper method on that string and you'd get back a brand new string object. And so the other 99 variables would still be pointing to the original string.

Therefore, Python can afford to keep only one object in memory, at least when it comes to immutable types. Any references to immutable data types will always reference the same object.
```python
a = 1
b = 1

print(a == b) # True
print(a is b) # True -> means that it is the same object in memory

a = "hello"
b = "hello"

print(a == b) # True
print(a is b) # True # True -> means that it is the same object in memory
```

# Shallow vs. Deep Copy

A shallow copy only creates a copy of the outermost level or layer of an object. In comparison, a deep copy recursively creates copies of all internal nested objects, down any number of levels. It is a more "complete" copy.
## Shallow Copy

Use it when there are not nested objects (e.g., list inside a list)

There three ways to create a shallow copy:
```python
a = [1, 2, 3]
b = a[:]

print(a == b) # True
print(a is b) # False

c = a.copy() # shallow copy -> creates a new list with the same elements

print(a == c) # True
print(a is c) # False

d = copy.copy(a) # shallow copy -> creates a new list with the same elements

print(a == d) # True
print(a is d) # False
```

However, it does not work with nested objects:
```python
numbers = [2, 3, 4]
a = [1, numbers, 5]
b = a.copy() # a[:] or copy.copy(a)

print(a == b) # True
print(a is b) # False

print(a[1] == b[1]) # True
print(a[1] is b[1]) # True -> the nested list is the same object in memory!

a[1].append(6)
print(a) # [1, [2, 3, 4, 6], 5]
print(b) # [1, [2, 3, 4, 6], 5]
```

## Deep Copy

Creates new objects in memory for the nested objects
```python
numbers = [2, 3, 4]
a = [1, numbers, 5]
b = copy.deepcopy(a)

print(a == b) # True
print(a is b) # False
print(a[1] == b[1]) # True
print(a[1] is b[1]) # False -> the nested list is a different object in memory

a[1].append(7)
print(a) # [1, [2, 3, 4, 7], 5]
print(b) # [1, [2, 3, 4], 5]
```