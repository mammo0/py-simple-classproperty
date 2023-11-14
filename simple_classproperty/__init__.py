"""
This module provides a simple implementation of a class property.
"""
from typing import Any

from .classproperty_decorator import _classproperty
from .classproperty_meta import _ClasspropertyMeta

__all__ = ["classproperty", "ClasspropertyMeta"]


# pylint: disable=C0103
class classproperty(_classproperty):
    def __getattr__(self, name: str) -> Any: ...


class ClasspropertyMeta(_ClasspropertyMeta):
    pass
