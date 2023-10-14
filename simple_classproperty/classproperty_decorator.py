from typing import Any, Optional, Union


class _classproperty(property):
    """
    The use this class as a decorator for your class property.

    Example:
        @classproperty
        def prop(cls):
            return "value"
    """
    # def __get__(self, *args, **_) -> Any:
    def __get__(self, instance: Any, owner: Optional[type]=None) -> Any:
        """
        This method gets called when a property value is requested.
        @return: The value of the property.
        """
        if instance is not None:
            return super().__get__(self.__get_class(instance), owner)

        return super().__get__(owner)

    def __set__(self, instance: Any, value: Any) -> None:
        """
        This method gets called when a property value should be set.
        @param cls_or_instance: The class or instance of which the property should be changed.
        @param value: The new value.
        """
        # call this method only on the class, not the instance
        super().__set__(self.__get_class(instance), value)

    def __delete__(self, instance: Any) -> None:
        """
        This method gets called when a property should be deleted.
        @param cls_or_instance: The class or instance of which the property should be deleted.
        """
        # call this method only on the class, not the instance
        super().__delete__(self.__get_class(instance))

    def __get_class(self, cls_or_instance: Union[type, object]) -> type:
        """
        Get the class of an object if one is provided.
        @param cls_or_instance: Either an object or a class.
        @return: The class of the object or just the class again.
        """
        if isinstance(cls_or_instance, type):
            return cls_or_instance

        return type(cls_or_instance)
