from datastructs.arrays.SingleDimensionArray import SingleDimensionArray as array
import unittest

from datastructs.exceptions.custom import (
                        InvalidArraySize,
                        InvalidDataType,
                        InvalidArrayIndex,
                        InvalidArrayInitializerSize
                        )


class TestArray(unittest.TestCase):


    def test_1d_Array(self):
        self.assertRaises(InvalidArrayInitializerSize, array, int, 1, [1,2])

        self.assertRaises(InvalidArrayInitializerSize, array, int, 2, [1])


        self.assertRaises(InvalidDataType, array, str, 1, [1])

        self.assertRaises(InvalidDataType, array, int, 2, [1,"12"])

        ar = array(int, 5, [1, 2, 3, 4, 5])
        ar.update(1, 99)
        self.assertEqual(ar.get(0), 1)
        self.assertEqual(ar.get(1), 99)

        self.assertRaises(InvalidDataType, ar.update, 1, "0")
        self.assertRaises(InvalidArrayIndex, ar.update, -1, 0)
        self.assertRaises(InvalidArrayIndex, ar.update, 1000, 0)
        self.assertRaises(InvalidArrayIndex, ar.get, 1000)
        self.assertRaises(InvalidArrayIndex, ar.get, -1)


if __name__ == '__main__':
    unittest.main()
