#!/usr/bin/env python
# -*- coding:utf8 -*-
# Copyright (c) Fred
# Licensed under GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

"""notes for frequently used functionalities of unittest"""

import unittest


class ClassSample:  # ClassSample(object)
    """sample class"""

    def __init__(self, mfoo=2, mbar=False):
        """ctor"""
        self.mfoo = mfoo  # pylint expects name not less than 3 characters
        self.mbar = mbar

    def get_mfoo(self):
        """function doc"""
        return self.mfoo

    def get_mbar(self):
        """function doc"""
        return self.mbar


class TestClassSampleMethods(unittest.TestCase):
    """refer to the doc for more ut functions"""

    def setUp(self):
        """function doc"""
        self.class_sample = ClassSample(1, True)

    def test_ctor(self):
        """function doc"""
        self.assertIsInstance(self.class_sample, ClassSample)
        self.assertEqual(self.class_sample.mfoo, 1)
        self.assertEqual(self.class_sample.mbar, True)

    def test_num(self):
        """function doc"""
        self.assertEqual(self.class_sample.get_mfoo(), 1)
        self.assertLess(1, 2)
        self.assertLessEqual(1, 2)
        self.assertGreater(2, 1)
        self.assertGreaterEqual(2, 1)
        self.assertNotEqual(2, 3)
        self.assertIsNotNone(1)
        self.assertIsNot(1, 2)
        self.assertIn(2, [1, 2])
        self.assertCountEqual([1, 2], [2, 1])

    def test_mfoo_bool(self):
        """function doc"""
        self.assertTrue(self.class_sample.get_mbar())
        self.assertFalse(not self.class_sample.get_mbar())

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        """for skipIf and skipUnless, refer to the doc"""
        self.fail("shouldn't happen")

    @unittest.expectedFailure
    def test_fail(self):
        """function doc"""
        self.assertEqual(1, 0, "expected failure case")

    def tearDown(self):
        """function doc"""
        print("tearDown")


# py -3 xxx.py -v: Verbose output for unittest
if __name__ == "__main__":
    unittest.main()
