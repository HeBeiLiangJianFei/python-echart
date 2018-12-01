# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Singleton(object):

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singletom, cls)
            cls._instance = orig.__new__(cls, *args, **kw)

        return cls._instance


class Myclass(Singleton):
    a = 1


class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class Myclass2(Borg):
    a = 1


def singleton(cls, *args, **kw):
