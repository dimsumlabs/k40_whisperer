
""" Perform unit tests on the egv.py file
"""


import unittest

import egv

class TestegvClass(unittest.TestCase):
    def setUp(self):
        self.data = []
        self.object = egv.egv(target=lambda s:self.data.append(s))

    def tearDown(self):
        self.object = None

#
# This file has a syntax error in OneWireCRC - the return tries to return
# an undefined variable.
#
# Thus - assume that function is unused for the moment
#
#    def test_OneWireCRC(self):
#        self.assertEqual(
#            self.object.OneWireCRC([fixme]),
#            fixme
#        )

    def test_make_move_data(self):

        tests = [
            { 'x': 0, 'y': 0, 'expect': '' },
            { 'x': 1, 'y': 1, 'expect': 'ILaBaS1P' },
            { 'x': 1000, 'y': 1000, 'expect': 'ILzzz235Bzzz235S1P' },
        ]
        # TODO - add more tests to demonstrate the edge cases

        for test in tests:
            self.data = []
            self.object.make_move_data( test['x'], test['y'] )
            got = "".join(map(chr, self.data))
            self.assertEqual( got, test['expect'] )
