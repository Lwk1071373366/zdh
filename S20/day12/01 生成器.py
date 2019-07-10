# def func():
#     print(1)
#     yield 6
#     print(6)
#     yield 9
# g=func()
# print(g.__next__())
# print(g.__next__())
#
# def func():
#     print(1)
#     yield 6
#     print(6)
#     yield 9
#
# g=func()
# print(func().__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

def func():
    print(1)
    a=yield 2
    print(a)
    print(3)
    b=yield 4
    print(b)
    c=yield 5
    print(c)
g=func()
# print(g.send(None))
# print(g.__next__())
print(g.__next__())
print(g.send('111'))
print(g.send(222))

