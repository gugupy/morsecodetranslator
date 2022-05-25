import unittest

from morcecodetranslator.morce import MorceCodeTranslator

morce_code = '....   .- .-   ..       ....   .- .-   ..'
message = 'HAAI HAAI'
mct = MorceCodeTranslator()

class TestMorceCode(unittest.TestCase):

    def test_encript(self):
        self.assertEqual(morce_code, mct.encript(message))

    def test_decript(self):
        self.assertEqual(message, mct.decript(morce_code))

    def test_decript_leading_7space(self):
        self.assertEqual(message, mct.decript(morce_code + '       '))
