# -*- coding : utf-8 -*-

from copy import deepcopy


class CopyableMixin:

    def copy(self):
        return deepcopy(self)
