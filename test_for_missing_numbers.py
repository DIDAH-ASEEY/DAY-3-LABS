import unittest
import missing_number

class MissingNumberTest(unittest.TestCase):
    """docstring for MissingNumberTest"""

    def test_empty_list(self):
        self.assertEqual(0, missing_number.find_missing([], []),
                         msg='should return 0 for empty list')

    def test_same_entries(self):
        list1 = missing_number.find_missing([2], [2])
        list2 = missing_number.find_missing([4], [4])
        list3 = missing_number.find_missing([7], [7])
        self.assertListEqual([0, 0, 0],
                             [list1, list2, list3],
                             msg='should return 0 for lists with the same entries')

    def test_missing_entries(self):
        list1 = missing_number.find_missing([1, 2], [1, 2, 5])
        list2 = missing_number.find_missing([4, 6, 8], [4, 6, 8, 10])
        list3 = missing_number.find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
        self.assertListEqual([5, 10, 1],
                             [list1, list2, list3],
                             msg='should return the missing number for lists with similar entries and a missing number')


if __name__=='__main__':
    unittest.main()
