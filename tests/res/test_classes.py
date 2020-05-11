from simple_classproperty import ClassPropertyMeta, classproperty


class TestClass(metaclass=ClassPropertyMeta):
    _ro_attr = "read-only"
    _rw_attr = "change_me"

    @classproperty
    def ro_attr(cls):
        return cls._ro_attr

    @classproperty
    def rw_attr(cls):
        return cls._rw_attr

    @rw_attr.setter
    def rw_attr(cls, value):
        cls._rw_attr = value

    @rw_attr.deleter
    def rw_attr(cls):
        del cls._rw_attr
