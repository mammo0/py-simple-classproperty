from functools import WRAPPER_ASSIGNMENTS


class _classproperty(property):
    """
    The use this class as a decorator for your class property.

    Example:
        @classproperty
        def prop(cls):
            return "value"
    """
    def __init__(self, *functions) -> None:
        """
        Preserve the original attributes of the decorated function.

        Avoids this issue: https://stackoverflow.com/questions/43544954/
                           why-does-sphinx-autodoc-output-a-decorators-docstring-when-there-are-two-decora
        """
        # the property __init__ method gets up to 4 functions as arguments
        # this is because of the special 'setter' and 'deleter' decorators
        for f in functions:
            if f:
                # use the functools for the arguments to perserve
                for attr in WRAPPER_ASSIGNMENTS:
                    if hasattr(f, attr):
                        setattr(self, attr, getattr(f, attr))

        super(_classproperty, self).__init__(*functions)

    def __get__(self, _, cls) -> object:
        """
        This method gets called when a property value is requested.
        @param cls: The class type of the above instance.
        @return: The value of the property.
        """
        # apply the __get__ on the class
        return super(_classproperty, self).__get__(cls)

    def __set__(self, cls_or_instance, value: object) -> None:
        """
        This method gets called when a property value should be set.
        @param cls_or_instance: The class or instance of which the property should be changed.
        @param value: The new value.
        """
        # call this method only on the class, not the instance
        super(_classproperty, self).__set__(self.__get_class(cls_or_instance), value)

    def __delete__(self, cls_or_instance) -> None:
        """
        This method gets called when a property should be deleted.
        @param cls_or_instance: The class or instance of which the property should be deleted.
        """
        # call this method only on the class, not the instance
        super(_classproperty, self).__delete__(self.__get_class(cls_or_instance))

    def __get_class(self, cls_or_instance) -> type:
        """
        Get the class of an object if one is provided.
        @param cls_or_instance: Either an object or a class.
        @return: The class of the object or just the class again.
        """
        if isinstance(cls_or_instance, type):
            return cls_or_instance
        else:
            return type(cls_or_instance)
