# Simple Python `classproperty` decorator

![PyPI package](https://github.com/mammo0/py-simple-classproperty/workflows/PyPI%20package/badge.svg)
[![PyPI version](https://badge.fury.io/py/simple-classproperty.svg)](https://badge.fury.io/py/simple-classproperty)

This module provides a simple way for defining class properties.


----

**Deprecation notice:** Starting with Python 3.9 the `@classmethod` descriptor can now wrap other descriptors like `@property`. See the official documentation for the announcement: https://docs.python.org/3.9/library/functions.html#classmethod

This means if you are using Python >= 3.9 you can simply realize a classproperty with:

```python
class NewClass():
    _atr = "val"

    @classmethod
    @property
    def attr(cls):
        return cls._atr
```

So in this case this package is not needed anymore. I will still try to maintain this package until Python 3.8 reaches EOL which will be in October 2024.

----


### Install

You can install this Python module via **pip**:
```shell
pip install simple-classproperty
```

Otherwise the module can be downloaded from PyPI: https://pypi.org/project/simple-classproperty/


### Usage

1. Import the module:
   ```python
   from simple_classproperty import ClasspropertyMeta, classproperty
   ```
2. Create a class with a class property:
   ```python
   class NewClass(metaclass=ClasspropertyMeta):
       _attr = "val"

       @classproperty
       def attr(cls):
           return cls._attr
   ```
   **Don't forget to set the `metaclass`!**
3. **(Optional)** Define also a setter and deleter for the newly created class property (this works like the standard python `property`):
   ```python
   @attr.setter
   def attr(cls, value):
       cls._attr = value

   @attr.deleter
   def attr(cls):
       del cls._attr
   ```


### Tips

The `classproperty` is also accessible from an instance:
```python
instance = NewClass()
print(instance.attr)  # "val"
```

When the value of the property is changed from an instance object, the class property will be changed. All other instances will have this new value:
```python
instance1 = NewClass()
instance2 = NewClass()

instance1.attr = "new"

print(instance1.attr)  # "new"
print(instance2.attr)  # "new"
print(NewClass.attr)   # "new"
```

This behavior is the same when a property gets deleted from an instance.
