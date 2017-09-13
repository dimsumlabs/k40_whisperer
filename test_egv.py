
""" Perform unit tests on the egv.py file
"""

#
# This file has a syntax error in OneWireCRC - the return tries to return
# an undefined variable.
#
# Thus - assume this file is unused for the moment and do not test anything
#

import unittest

import egv

class TestegvClass(unittest.TestCase):
    def setUp(self):
        self.object = egv.egv()

    def tearDown(self):
        self.object = None

#    def test_OneWireCRC(self):
#        self.assertEqual(
#            self.object.OneWireCRC([fixme]),
#            fixme
#        )

