## Definition
A script describes a Python file that is meant to be executed directly
A module describes a Python file that is meant to be executed by other files. 

Modules isolate the logic to a specific files

```python
# my-file-name.py
# __name__ -> my-file-name, if the file is executed as a module
# __name__ -> __main__, if the file is executed as a script
```

Note:
If a variable name is preceded by double underscore, it cannot be accessed from outside the file. In other words, if the file is imported as a module in another file, this variable will not be accessible:
```python
# file1.py
age = 28
__year = 2024

# file2.py
import file1 as f1
print(f1.age)  # 28
# print(f1.year)  # NameError: name 'year' is not defined
```
## Standard Library
A collection of tools built into a language to accelerate developer productivity


