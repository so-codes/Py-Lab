# Dictionary methods

1 - Update

dict.update(other) updates the dictionary with the key/value pairs from other, overwriting existing keys:
```python
>>> d = {'a': 1, 'b': 2}
>>> d.update({'b': 3, 'c': 4})
>>> d
{'a': 1, 'b': 3, 'c': 4}
```


2 - Get

dict.get(key[, default]) returns the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError:
```python
>>> d = {'a': 1, 'b': 2}
>>> d.get('b')
2
>>> d.get('c')
>>> d.get('c', 3)
3
```


3 - Pop

dict.pop(key[, default]) removes the item with key and returns its value or default if key is not found. If default is not given and key is not in the dictionary, a KeyError is raised:
```python
>>> d = {'a': 1, 'b': 2}
>>> d.pop('b')
2
>>> d
{'a': 1}
>>> d.pop('c')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'
>>> d.pop('c', 3)
3
```


4 - Popitem

dict.popitem() removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty:
```python
>>> d = {'a': 1, 'b': 2}
>>> d.popitem()
('b', 2)
>>> d
{'a': 1}
>>> d.popitem()
('a', 1)
>>> d
{}
>>> d.popitem()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'popitem(): dictionary is empty'
```


5 - Clear

dict.clear() removes all items from the dictionary:
```python
>>> d = {'a': 1, 'b': 2}
>>> d.clear()
>>> d
{}
```