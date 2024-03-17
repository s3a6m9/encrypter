""" Command-line usage of the encrypter package """
import argparse
from .encrypter import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="encrypter", description="Encrypt or decrypt files/folders.")
    parser.add_argument("path", type=str, help="Path to the file/folder.")
    parser.add_argument("--exclude", type=str, help="Comma-separated list of files to exclude.")
    parser.add_argument("--output", type=str, help="Output directory for encrypted files/folders.")
    parser.add_argument("--decrypt", type=str, help="Add decryption key to decrypt file(s).")
    parser.add_argument("--suffix", type=str, help="Add a suffix to decrypt/encrypt paths with.")
    main(parser.parse_args())
