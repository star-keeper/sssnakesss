import unittest

from s1c01 import b64ToHex, hexToB64
from s1c02 import xor
from s1c03 import solveS1C03, caesarEncrypt, caesarDecrypt, scoreText
from s1c04 import solveS1C04
from s1c05 import vigenereEncrypt, vigenereDecrypt
from s1c06 import editDistance, solveS1C06
from s1c07 import AES_ECB_encrypt, AES_ECB_decrypt
from s1c08 import solveS1C08

class TestLab2(unittest.TestCase):

    '''Here's an example of what some test cases might look like.'''

    def test_s1c01_hexToB64(self):
        testCases = [
            (
                b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
                b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
            ),
            (b'4e6f6e204d696e6973747261726920736564204d696e69737472617265', b'Tm9uIE1pbmlzdHJhcmkgc2VkIE1pbmlzdHJhcmU='),
            (b'', b''),
            (b'61', b'YQ=='),
            (b'6666666664643435', b'ZmZmZmRkNDU=')

        ]
        for hexString, b64String in testCases:
            self.assertEqual(hexToB64(hexString), b64String)
            self.assertEqual(type(hexToB64(hexString)), str)

    '''One more example.'''

    def test_s1c01_b64ToHex(self):
        testCases = [
            (
                b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
                b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
            ),
            (b'4e6f6e204d696e6973747261726920736564204d696e69737472617265', b'Tm9uIE1pbmlzdHJhcmkgc2VkIE1pbmlzdHJhcmU='),
            (b'', b''),
            (b'61', b'YQ=='),
            (b'6666666664643435', b'ZmZmZmRkNDU=')

        ]
        for hexString, b64String in testCases:
            self.assertEqual(b64ToHex(b64String), hexString)

    @unittest.skip('Not yet implemented')
    def test_s1c02_xor(self):
        '''
        Starting here, write your own tests. You can generate tests in a variety
        of ways, ranging from trivial tests (does the empty string produce the empty
        string?) to tests of properties (does xor preserve length?) to tests of types
        (is the return type of this method correct?) to specific cases (is the xor
        of these two specific byte strings equal to the correct byte string?).

        To generate specific cases, I'd suggest either using very small examples 
        you can work by hand, or generate the test cases using other code you write
        or online calculators.
        '''
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c03_caesarEncrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c03_caesarDecrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c03_scoreText(self):
        self.assertEqual(True, False)


    '''
       ********
       Remember! You can and should add more test methods to this file to test 
       other helper methods that you write in the course of this lab.
       ********
    '''


    @unittest.skip('Not yet implemented')
    def test_s1c03_solveS1C3(self):
        '''
        You might find that it's less clear what the testable contract of the methods
        that just solve the challenges is. If you choose, you can decide not to use
        this test method, and instead just test the helper methods you write to make
        solveSXCY() methods work.
        '''
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c04_solveS1C4(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c05_vigenereEncrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c05_vigenereDecrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c06_editDistance(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c06_solveS1C6(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c07_AES_ECB_encrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c07_AES_ECB_decrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c08_solveS1C8(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
