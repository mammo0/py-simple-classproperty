from simple_classproperty import ClasspropertyMeta, classproperty


class TestClass(metaclass=ClasspropertyMeta):
    _ro_attr: str = "read-only"
    _rw_attr: str = "change_me"

    @classproperty
    def ro_attr(cls) -> str:
        return cls._ro_attr

    @classproperty
    def rw_attr(cls) -> str:
        return cls._rw_attr

    @rw_attr.setter
    def rw_attr(cls, value) -> None:
        cls._rw_attr = value

    @rw_attr.deleter
    def rw_attr(cls) -> None:
        del cls._rw_attr
