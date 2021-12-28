from unittest import TestCase
from copy import copy, deepcopy

class CPart8Test(TestCase):

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        print("======= ", self.id())

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        pass

    # 变量不是盒子， 而是便利贴
    def test_1(self):
        a = [1, 2, 3]
        b = a
        a.append(4)
        print(b)

    # 创建对象之后才会把变量分配给对象
    def test_2(self):
        try:
            print(dir())
            b = 0
            a = b / b
        except Exception as e:
            print(e)
        finally:
            print(dir())

    # is和==的区别
    def test_eq(self):
        a = [0]
        b = a
        print(a is b, a == b)
        a.append(1) # 同id的b一样变化
        print(a, b)
        a, b = [0], [0]
        print(a is b, a == b)
        a.append(1) # 不同id的b没有变化
        print(a, b)

    # == __eq__
    def test_eq2(self):
        class A:
            def __eq__(self, other):
                print("eq all")
                return True
        a = A()
        print(a == None)
        print(a == 1000)

    # 元组的相对不可变
    def test_tuple(self):
        a = (1, 2, [3, 4])
        a[-1].append(5)
        print(a)

    # 浅拷贝 内置的类型构造方法是浅拷贝
    def test_shallowcopy(self):
        a = [3, [1, 2]]
        b = list(a)
        a.append(3)
        print(a, b)
        a[1].append(3)
        print(a, b)

    # 深拷贝 借助www.pythontutor.com
    # deepcopy会记住已经复制的对象，所以能处理循环引用
    def test_deepcopy(self):
        a = [1, [2, 3]]
        b = [a, 1]
        a.append(b)
        ca = copy(a)
        cb = deepcopy(a)

    # 传参数
    def test_funcargs(self):
        def add(a):
            print("进入方法: ", id(a))
            a += a
            print("离开方法: ", id(a))
        b = 1
        print("b id:", id(b))
        add(b)
        print("b id:", id(b), b)

        b = [1]
        print("b id:", id(b))
        add(b)
        print("b id:", id(b), b)

    # 默认参数不要用可变对象
    def test_mutablearg(self):
        def f(d=[]):
            d.append(1)
            print(id(d))
            return d
        print(id(f.__defaults__[0]))
        print(f())
        print(f())

    # __del__
    def test_del(self):
        l = []
        class A(object):
            def __del__(self):
                print("__del__")
                l.append(self)
        a1 = A()
        del a1
        print(l)
        l.clear()
        print(l)


if __name__ == '__main__':
    CPart8Test()