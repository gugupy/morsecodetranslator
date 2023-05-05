import unittest

from morsecodetranslator.morse import MorseCodeTranslator

morce_code = '....   .- .-   ..       ....   .- .-   ..'
message = 'HAAI HAAI'
mct = MorseCodeTranslator()


class TestMorceCode(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(morce_code, mct.encrypt(message))

    def test_decrypt(self):
        self.assertEqual(message, mct.decrypt(morce_code))

    def test_decrypt_leading_7space(self):
        self.assertEqual(message, mct.decrypt(morce_code + '       '))
