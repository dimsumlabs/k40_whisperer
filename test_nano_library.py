
""" Perform unit tests on the nano_library.py file
"""

import unittest

import nano_library

class TestK40_CLASS(unittest.TestCase):
    def setUp(self):
        self.object = nano_library.K40_CLASS()

    def tearDown(self):
        self.object = None

    def test_constants(self):
        hello  = "".join(map(chr, self.object.hello))
        unlock = "".join(map(chr, self.object.unlock))
        home   = "".join(map(chr, self.object.home))
        estop  = "".join(map(chr, self.object.estop))

        self.assertEqual(hello,  '\xa0')
        self.assertEqual(unlock, '\xa6\x00IS2PFFFFFFFFFFFFFFFFFFFFFFFFFF\xa6\x0f')
        self.assertEqual(home,   '\xa6\x00IPPFFFFFFFFFFFFFFFFFFFFFFFFFFF\xa6\xe4')
        self.assertEqual(estop,  '\xa6\x00IFFFFFFFFFFFFFFFFFFFFFFFFFFFFF\xa6\x82')

    def test_OneWireCRC(self):
        line = map(ord, 'AK0FFFFFFFFFFFFFFFFFFFFFFFFFFF')

        # Do we get the expected CRC?
        self.assertEqual( self.object.OneWireCRC(line), 0xa4 )

        # Now, are the magic arrays simply normal packets with a valid CRC?
        self.assertEqual(
            self.object.OneWireCRC(self.object.unlock[1:-2]),
            self.object.unlock[-1] 
        )
        self.assertEqual(
            self.object.OneWireCRC(self.object.home[1:-2]),
            self.object.home[-1] 
        )
        self.assertEqual(
            self.object.OneWireCRC(self.object.estop[1:-2]),
            self.object.estop[-1] 
        )

