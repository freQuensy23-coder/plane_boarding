from unittest import TestCase
from main import mov

class TestMov(TestCase):
    def test_mov_simple(self):
        arr1 = [1, None, 3]
        mov(arr1, 0, arr1, 1)
        assert arr1 == [None, 1, 3]

    def test_mov_2_arrays(self):
        arr1 = [1, 2, 3]
        arr2 = [None]
        mov(arr1, 1, arr2, 0)
        assert arr2 == [2]
        assert arr1 == [1, None, 3]

    def test_mov_not_none(self):
        arr1 = [1, 2, 3]
        with self.assertRaises(Exception):
            mov(arr1, 0, arr1, 2)