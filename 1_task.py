class FlatIterator:

    def __init__(self, list_of_list):
        self.items_list = sum(list_of_list, [])
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter != len(self.items_list):
            item = self.items_list[self.counter]
            self.counter += 1

            return item
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()