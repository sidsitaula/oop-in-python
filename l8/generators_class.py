# import random
# choice = ['roxxane\n', 'mood\n']
# seq = (random.choice(choice) for i in range(100))
# print(seq)

# with open('sql.txt', 'w') as f:
#     for s in seq:
#         f.write(s)

class Filter:
    def __init__(self, inf):
        self.inf = inf

    def __iter__(self):
        return self

    def __next__(self):
        l = self.inf.readline()
        while l and 'mood' not in l:
            l = self.inf.readline()
        if not l:
            raise StopIteration()
        return l.replace('mood', 'moood')


def filter(seq):
    for i in seq:
        if 'mood' in i:
            yield 'moood\n'


res_1 = []
res_2 = []
with open('sql.txt', 'r') as inf:
    for line in Filter(inf):
        res_1.append(line)
with open('sql.txt', 'r') as inf:
    for line in filter(inf):
        res_2.append(line)

print(res_1 == res_2)
