```python
# sys.arg read all inputs in the command line AFTER python3 keyword (including the python file name)
import sys

print(sys.argv)
print(type(sys.argv))

arguments = sys.argv

total_length = 0
for argument in arguments[1:]:
	total_length += len(argument)

print("The total length of the arguments is", total_length)
```
output
```python
python3 command-line-arguments-with-argv.py 3 marios True
['command-line-arguments-with-argv.py', '3', 'marios', 'True']
<class 'list'>
The total length of the arguments is 11
```