# class A:
#     __flag = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__flag is None:
#             cls.__flag = object.__new__(cls)
#         return cls.__flag
#     def __init__(self,name=None,age = None):
#         self.name = name
#         if age :
#             self.age = age
# a1 = A('alex',84)
# print(a1)
# a2 = A('alex',83)
# print(a2)
# a3 = A('alex')
# print(a3)
# print(a1.age)

# class A:
#     __flag = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__flag is None:
#             cls.__flag = object.__new__(cls)
#         return cls.__flag
#     def __init__(self,name = None,age = None):
#         self.name = name
#         if age :
#             self.age = age
# a1 = A('alex',83)
# print(a1)
# a2 = A('alex',82)
# print(a2)
# a3 = A('alex')
# print(a3)
# print(a1.age)
