from typing import Optional

from .classproperty_decorator import _classproperty as classproperty


class _ClasspropertyMeta(type):
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
        cp_obj: Optional[classproperty] = self.__get_classproperty_attr(name)
        if cp_obj:
            cp_obj.__set__(self, value)
        else:
            super(_ClasspropertyMeta, self).__setattr__(name, value)

    def __delattr__(self, name: str):
        """
        Override of __delattr__ method to allow a classproperty.deleter.
        @param str: The name of the attribute to delete.
        """
        cp_obj: Optional[classproperty] = self.__get_classproperty_attr(name)
        if cp_obj:
            cp_obj.__delete__(self)
        else:
            super(_ClasspropertyMeta, self).__delattr__(name)

    def __get_classproperty_attr(self, name: str) -> Optional[classproperty]:
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
