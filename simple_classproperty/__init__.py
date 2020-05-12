"""
This module provides a simple implementation of a class property.
"""
from simple_classproperty.classproperty_decorator import _classproperty
from simple_classproperty.classproperty_meta import _ClasspropertyMeta


__all__ = ["classproperty", "ClassPropertyMeta"]


classproperty = _classproperty
ClassPropertyMeta = _ClasspropertyMeta
