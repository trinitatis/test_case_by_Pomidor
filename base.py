'''
    Parent
    /   \
First    Second
    \   /
     A|B
'''
class MyError(Exception):
    def __str__(self):
        return "Error text"

class Parent:
    def __init__(self, i: int | None, first: bool = False) -> None:
        if i == None: i = 3
        self.i = i
        self.first = first

    def fnc(self, arg_1: int | None = None,
                  arg_2: int | None  = None) -> int:
        if arg_1 == None: arg_1 = 1
        if arg_2 == None: arg_2 = arg_1
        if arg_1 == 7: raise MyError
        return arg_1 * arg_2 * self.i

    @property
    def isFirst(self):
        return self._isFirst

    @property
    def isSecond(self):
        return self._isSecond

    def _isFirst(self):
        return self.first

    def _isSecond(self):
        return not self.first

   
class First(Parent):
    instances = 0
    def __init__(self, *args, **kwargs):
        first = False
        if not First.instances:
            first = True
            First.instances += 1
        super().__init__(*args, first, **kwargs)


class Second(Parent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)






































