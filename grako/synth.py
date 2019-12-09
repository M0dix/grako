# -*- coding: utf-8 -*-
# Copyright (C) 2017      by Juancarlo Añez
# Copyright (C) 2012-2016 by Juancarlo Añez and Thomas Bragg
__REGISTRY = vars()


class _Synthetic(object):
    def __reduce__(self):
        return (
            synthesize(type(self).__name__, type(self).__bases__),
            (),
            vars(self),
        )


def synthesize(name, bases):
    typename = '%s.%s' % (__name__, name)

    if not isinstance(bases, tuple):
        bases = (bases,)

    if _Synthetic not in bases:
        bases = (_Synthetic,) + bases

    constructor = __REGISTRY.get(typename)
    if not constructor:
        constructor = type(name, bases, {})
        typename = constructor.__name__
        __REGISTRY[typename] = constructor

    return constructor
