from collections import defaultdict


class Counter:
    count = 0

    def increase(self):
        self.count += 1
        return self.count


d = defaultdict(Counter().increase)
