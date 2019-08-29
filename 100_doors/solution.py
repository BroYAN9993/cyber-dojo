class Doors(object):
    def __init__(self, target):
        self.target = target
        self._open = set()
        self._closed = set(range(1, target + 1))

    def _toogle(self, num):
        if num in self._open:
            self._open.remove(num)
            self._closed.add(num)
        else:
            self._closed.remove(num)
            self._open.add(num)

    def _visit(self, num):
        for i in range(1, self.target + 1):
            if not i % num:
                self._toogle(i)

    def get_result(self):
        for n in range(1, 101):
            self._visit(n)
        print(f"open: {sorted(list(self._open))}, \nclosed: {sorted(list(self._closed))}")
        return self._open, self._closed


def main():
    d = Doors(100)
    d.get_result()


if __name__ == '__main__':
    main()
