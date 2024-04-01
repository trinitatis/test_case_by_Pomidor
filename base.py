class MyError(Exception):
    def __str__(self):
        return "Error text"


class First:  pass


class Second:   pass


class Parent:
    instances = False
    
    def __init__(self, i: int  | None) -> None:
        ''' Dinamic rebuilding the inheritance hierarchy:
        first created <Parent> instance will also be <First> instance,
        The next <Parent> instance will be <Second> instance.
        '''
        cls_base = self.__class__.__base__
        if not Parent.instances:
            Parent.instances = True        
            self.__class__.__bases__ = (First, cls_base)
        else:
            self.__class__.__bases__ = (Second, cls_base)

        if not i: i = 3
        self.i = i

  
    def fnc(self, arg1: int = 1, arg2: int | None = None) -> int:
        if not arg2:
            arg2 = arg1

        if arg1 == 7: raise MyError
            
        return arg1 * arg2 * self.i

    def isFirst(self):
        return isinstance(self, First)
    
    @property
    def isSecond(self):
        return isinstance(self, Second)
