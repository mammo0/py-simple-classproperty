"""
This module provides a simple implementation of a class property.
"""
from .classproperty_decorator import _classproperty
from .classproperty_meta import _ClasspropertyMeta


__all__ = ["classproperty", "ClasspropertyMeta"]


class classproperty(_classproperty):
    pass


class ClasspropertyMeta(_ClasspropertyMeta):
    pass
