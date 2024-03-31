from base import *


class B(First, Second):

    def __init__(self, i: int | None = None):
        super().__init__(i)
