class NegExt:
    def __neg__(self):
        for cls in self.__class__.mro():
            if cls is NegExt or cls is self.__class__ or cls is object:
                continue
            if hasattr(cls, '__neg__'):
                return self.__class__(cls.__neg__(self)) 
        
            elif hasattr(cls, '__getitem__') and not cls is dict:
                return self.__class__(self[1:-1])
            else:
                return self.__class__(self)

