import inspect
import sys

def introspection_info(obj1, obj2):
    return obj1, obj2

ff = introspection_info(obj1=42, obj2='Hello')
print(ff)
print('*' * 30)
print('тип:', type(ff))
print('*' * 30)
print('модули атрибуты:',dir(ff))
print('*' * 30)
print(type(ff) is int)
print('*' * 30)
print(hasattr(ff, 'count'))
print('*' * 30)
print(getattr(ff, 'get1111', 'sdfgsegt'))
print('*' * 30)
print(callable(ff))
print('*' * 30)
print(inspect.isclass(ff))
print('*' * 30)
print(inspect.ismodule(ff))
print('*' * 30)
print(inspect.getmodule(ff))
print('*' * 30)
print(dir(sys))
print('*' * 30)
print(sys.executable)
print('*' * 30)
print(sys.platform)
print('*' * 30)
print(sys.version)
print('*' * 30)
print(sys.version_info)
print('*' * 30)
print(sys.path)
print('*' * 30)
print(sys.modules)
print('*' * 30)
print(sys.argv)



