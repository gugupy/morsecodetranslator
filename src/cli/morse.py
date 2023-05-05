from argparse import ArgumentParser

from morsecodetranslator.morse import MorseCodeTranslator

mct = MorseCodeTranslator()


def encrypt(args):
    if args.text:
        print(f'Morse Code: {mct.encrypt(args.text)}')


def decrypt(args):
    if args.morse_text:
        print(f'Plain Text: {mct.decrypt(args.morse_text)}')


# Initializing ArgumentParser for morse command
morse = ArgumentParser(
    prog='morse',
    description='Convert plain text to morse code and vise-versa.',
    epilog='Morse Code Converter',
)

# Initializing subparsers to create sub-commands
morse_subparser = morse.add_subparsers(help='sub-commands')

# encrypt subcommand and arguments
encrypt_parser = morse_subparser.add_parser('encrypt')
encrypt_parser.set_defaults(func=encrypt)
encrypt_parser.add_argument(
    '--text',
    required=True,
    default='MORSE CODE',
    help='Text to convert morse code',
)

# decrypt subcommand and arguments
decrypt_parser = morse_subparser.add_parser('decrypt')
decrypt_parser.set_defaults(func=decrypt)
decrypt_parser.add_argument(
    '--morse-text',
    required=True,
    default='',
    help='Morse code to convert text.',
)


def main():
    args = morse.parse_args()
    try:
        args.func(args)
    except AttributeError:
        morse.print_help()
