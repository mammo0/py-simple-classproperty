# Simple Python `classproperty` decorator

![PyPI package](https://github.com/mammo0/py-simple-classproperty/workflows/PyPI%20package/badge.svg)

This module provides a simple way for defining class properties.


### Install

You can install this Python module via **pip**:
```shell
pip install simple-classproperty
```

Otherwise the module can be downloaded from PyPI: *TODO*


### Usage

1. Import the module:
   ```python
   from simple_classproperty import ClassPropertyMeta, classproperty
   ```
2. Create a class with a class property:
   ```python
   class NewClass(metaclass=ClassPropertyMeta):
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

But when the value of the property is changed from an instance object, only the instance has this value:
```python
instance = NewClass()
instance.attr = "new"
print(instance.attr)  # "new"
print(NewClass.attr)  # "val"
```

When deleting the property from the instance, the class value is used again:
 ```python
instance = NewClass()
instance.attr = "new"
print(instance.attr)  # "new"

del instance.attr
print(instance.attr)  # "val"
```
