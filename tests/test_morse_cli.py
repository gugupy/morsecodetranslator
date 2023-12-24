import unittest
import subprocess


morse_code = "....   .- .-   ..       ....   .- .-   .."
message = "HAAI HAAI"


class TestMorseCodeCLI(unittest.TestCase):
    def test_encrypt_cli(self):
        output = subprocess.run(
            ["morse", "encrypt", "--text", message], capture_output=True
        )
        self.assertEqual(
            f"Morse Code: {morse_code}", output.stdout.decode("utf-8").rstrip()
        )

    def test_decrypt_cli(self):
        output = subprocess.run(
            ["morse", "decrypt", "--morse-text", morse_code], capture_output=True
        )
        self.assertEqual(
            f"Plain Text: {message}", output.stdout.decode("utf-8").rstrip()
        )
