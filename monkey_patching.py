class Test:
    pass


def setter(self, value):
    self.value = value


def getter(self):
    print(self.value)


Test.setter = setter
Test.getter = getter

Test.gunman = 'Sid'

s = Test()
s.setter(12)
s.getter()
print(s.gunman)
