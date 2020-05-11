"""
This module provides a simple implementation of a class property.
"""


class classproperty(property):
    """
    The use this class as a decorator for your class property.

    Example:
        @classproperty
        def prop(self):
            return "value"
    """
    def __get__(self, instance, cls) -> object:
        """
        This method gets called when a property value is requested.
        @param instance: The instance with the property.
        @param cls: The class type of the above instance.
        @return: The value of the property.
        """
        # if an instance is provided, use it
        if instance is not None:
            return super(classproperty, self).__get__(instance)
        # otherwise the class
        else:
            return super(classproperty, self).__get__(cls)


class ClassPropertyMeta(type):
    """
    The class that uses the classproperty decorator must use this meta class if the setting and deleting of a class
    property should be supported.
    """
    def __setattr__(self, name: str, value: object) -> None:
        """
        Override of __setattr__ method to allow a classproperty.setter.
        @param name: The name of the attribute that should get a new value.
        @param value: The new value of the attribute.
        """
        cp_obj = self.__get_classproperty_attr(name)
        if cp_obj:
            cp_obj.__set__(self, value)
        else:
            super(ClassPropertyMeta, self).__setattr__(name, value)

    def __delattr__(self, name: str):
        """
        Override of __delattr__ method to allow a classproperty.deleter.
        @param str: The name of the attribute to delete.
        """
        cp_obj = self.__get_classproperty_attr(name)
        if cp_obj:
            cp_obj.__delete__(self)
        else:
            super(ClassPropertyMeta, self).__delattr__(name)

    def __get_classproperty_attr(self, name: str) -> classproperty:
        """
        Get a classproperty attribute from this class with the given name.
        @param name: The name of the attribute.
        @return: The classproperty object for the attribute. Or 'None' if it wasn't found.
        """
        # iterate through MRO list to get all attributes
        if (name in self.__dict__ and
                # check if it's a classproperty attribute
                isinstance(self.__dict__[name], classproperty)):
            return self.__dict__[name]
        else:
            return None
