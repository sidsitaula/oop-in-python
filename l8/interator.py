class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)


class CapitalIterator:
    def __init__(self, strings):
        self.words = [w.capitalize() for w in strings.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self


iterable = CapitalIterable('hello world!')
iterator1 = iter(iterable)
iterator2 = iter(iterable)
for w in iterable:
    print(w)

while True:
    try:
        print(next(iterator1), next(iterator2))
    except StopIteration:
        break
