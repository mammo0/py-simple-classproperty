from typing import Any, Optional

from .classproperty_decorator import _classproperty as classproperty


class _ClasspropertyMeta(type):
    """
    The class that uses the classproperty decorator must use this meta class if the setting and deleting of a class
    property should be supported.
    """
    def __setattr__(cls, name: str, value: Any) -> None:
        """
        Override of __setattr__ method to allow a classproperty.setter.
        @param name: The name of the attribute that should get a new value.
        @param value: The new value of the attribute.
        """
        cp_obj: Optional[classproperty] = cls.__get_classproperty_attr(name)
        if cp_obj:
            cp_obj.__set__(cls, value)
        else:
            super().__setattr__(name, value)

    def __delattr__(cls, name: str):
        """
        Override of __delattr__ method to allow a classproperty.deleter.
        @param str: The name of the attribute to delete.
        """
        cp_obj: Optional[classproperty] = cls.__get_classproperty_attr(name)
        if cp_obj:
            cp_obj.__delete__(cls)
        else:
            super().__delattr__(name)

    def __get_classproperty_attr(cls, name: str) -> Optional[classproperty]:
        """
        Get a classproperty attribute from this class with the given name.
        @param name: The name of the attribute.
        @return: The classproperty object for the attribute. Or 'None' if it wasn't found.
        """
        # iterate through MRO list to get all attributes
        if (name in cls.__dict__ and
                # check if it's a classproperty attribute
                isinstance(cls.__dict__[name], classproperty)):
            return cls.__dict__[name]

        return None
