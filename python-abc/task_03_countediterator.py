#!/usr/bin/python3
"""CountedIterator class"""

class CountedIterator:
    """Iterator wrapper that counts how many items have been iterated"""

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Return the iterator itself"""
        return self

    def __next__(self):
        """Return the next item and increment counter"""
        try:
            item = next(self._iterator)
            self._count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """Return number of items iterated so far"""
        return self._count
