## E1

Define a length_counts function that accepts a list of strings. 
The function should return a dictionary where the keys represent
length and the values represent how many strings have that length.

Example:
```python
sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]

# length_counts(sa_countries) => {6: 1, 9: 2, 7: 2, 4: 1}
```

Solution:
```python
def length_counts(elements):
	counts = {}
	for element in elements:
		length = len(element)
		current_count = counts.get(length, 0)
		counts[length] = current_count + 1

return counts
```