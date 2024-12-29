from typing import Iterable


class FlatIterator:

    def __init__(self, list_of_list):
        self.flatten_list = flat(list_of_list)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.flatten_list):
            raise StopIteration
        else:
            return self.flatten_list[self.cursor]


def flat(element):
    if isinstance(element, Iterable) and not isinstance(element, str):
        return [a for i in element for a in flat(i)]
    else:
        return [element]


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()