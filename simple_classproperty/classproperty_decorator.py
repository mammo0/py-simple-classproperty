class _classproperty(property):
    """
    The use this class as a decorator for your class property.

    Example:
        @classproperty
        def prop(cls):
            return "value"
    """
    def __get__(self, *args, **_) -> object:
        """
        This method gets called when a property value is requested.
        @return: The value of the property.
        """
        # apply the __get__ on the class, which is the second argument
        return super(_classproperty, self).__get__(args[1])

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
