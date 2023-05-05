import unittest

from morsecodetranslator.morse import MorseCodeTranslator

morse_code = '....   .- .-   ..       ....   .- .-   ..'
message = 'HAAI HAAI'
mct = MorseCodeTranslator()


class TestMorseCode(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(morse_code, mct.encrypt(message))

    def test_decrypt(self):
        self.assertEqual(message, mct.decrypt(morse_code))

    def test_decrypt_leading_7space(self):
        self.assertEqual(message, mct.decrypt(morse_code + '       '))
