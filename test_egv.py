
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

    def test_move(self):

        tests = [
            { 'dir':        0, 'dist':  0, 'laser': False, 'expect': '' },
            { 'dir': ord('B'), 'dist':  1, 'laser': False, 'expect': 'Ba' },
            { 'dir': ord('T'), 'dist':  1, 'laser': False, 'expect': 'Ta' },
            { 'dir': ord('L'), 'dist':  1, 'laser': False, 'expect': 'La' },
            { 'dir': ord('R'), 'dist':  1, 'laser': False, 'expect': 'Ra' },
            { 'dir': ord('M'), 'dist':  1, 'laser': False, 'expect': 'Ma' },
            { 'dir':  0, 'dist':  0, 'laser': True,  'expect': 'D' },
            { 'dir':  0, 'dist':  0, 'laser': False, 'expect': 'U' },
        ]

        # TODO
        # - need to write code to exercise the angle_dirs, but I dont quite
        #   understand what they are trying to achieve yet

        for test in tests:
            self.data = []
            self.object.move( test['dir'], test['dist'], test['laser'] )
            self.object.flush()
            got = "".join(map(chr, self.data))
            self.assertEqual( got, test['expect'] )

    def test_flush(self):
        tests = [
            { 'laser': False, 'expect': '' },
            { 'laser': True,  'expect': 'D' },
            { 'laser': False, 'expect': 'U' },
        ]

        for test in tests:
            self.data = []
            self.object.flush(laser_on=test['laser'])
            got = "".join(map(chr, self.data))
            self.assertEqual( got, test['expect'] )

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

    def test_make_distance(self):
        with self.assertRaises(StandardError):
            self.object.make_distance(1.1)

        # What a strange number coding.  I guess they had never heard of
        # Huffman, or ASN.1 BER
        tests = [
            { 'mils':    0, 'expect': '' },
            { 'mils':    1, 'expect': 'a' },
            { 'mils':   25, 'expect': 'y' },
            { 'mils':   26, 'expect': '|a' },
            { 'mils':   51, 'expect': '|z' },
            { 'mils':   52, 'expect': '052' },
            { 'mils':  254, 'expect': '254' },
            { 'mils':  255, 'expect': 'z' },
            { 'mils':  256, 'expect': 'za' },
            { 'mils':  511, 'expect': 'zza' },
            { 'mils':  766, 'expect': 'zzza' },
            { 'mils': 1021, 'expect': 'zzzza' },
        ]

        for test in tests:
            got = "".join(map(chr, self.object.make_distance( test['mils'] )))
            self.assertEqual( got, test['expect'] )

    def test_make_dir_dist(self):

        tests = [
            { 'x':  0, 'y':  0, 'expect': '' },
            { 'x':  0, 'y':  1, 'expect': 'La' },       # Left
            { 'x':  0, 'y': -1, 'expect': 'Ra' },       # Right
            { 'x':  1, 'y':  0, 'expect': 'Ba' },       # Bottom
            { 'x': -1, 'y':  0, 'expect': 'Ta' },       # Top
        ]

        # make_dir_dist() is an up/down then left/right mover
        # TODO - test with laser_on=True (perhaps in test_move)

        for test in tests:
            self.data = []
            self.object.make_dir_dist( test['x'], test['y'] )
            self.object.flush()
            got = "".join(map(chr, self.data))
            self.assertEqual( got, test['expect'] )

#    def test_make_cut_line(self):

    def test_make_move_data(self):

        tests = [
            { 'x': 0, 'y': 0, 'expect': '' },
            { 'x': 1, 'y': 1, 'expect': 'ILaBaS1P' },
            { 'x': 1000, 'y': 1000, 'expect': 'ILzzz235Bzzz235S1P' },
        ]

        # make_move_data() is essentially a wrapper around make_distance():
        # "I" "L{}" "B{}" "S1P", with the two {} filled in by make_distance

        for test in tests:
            self.data = []
            self.object.make_move_data( test['x'], test['y'] )
            got = "".join(map(chr, self.data))
            self.assertEqual( got, test['expect'] )
