"""
Command-line python encrypter.
"""
import base64
from . import argparse
from . import os
from . import Fernet

def encrypt_file(path: str, out_path: str, fernet_object: Fernet):
    """Encrypts a file using the provided key."""
    with open(path, "rb") as file:
        file_data = file.read()

    with open(out_path, "wb") as file:
        file.write(fernet_object.encrypt(file_data))

def decrypt_file(path: str, out_path: str, fernet_object: Fernet):
    """Decrypts a file using the provided key."""
    with open(path, "rb") as file:
        encrypted_data = file.read()

    with open(out_path, "wb") as file:
        file.write(fernet_object.decrypt(encrypted_data))

def encrypt_recursively(path: str, out_path: str, fernet_object: Fernet, suffix: str, exclude: list):
    """ Encrypts folders recursively """
    output_root_path = os.path.join(out_path, os.path.basename(path) + suffix)
    output_prefix = os.path.split(output_root_path)[0]
    split_position = len(path.split("/")) - 1  # First item is empty because of path starting with /

    for path_collection in os.walk(path):
        root_path = os.path.join(
            output_prefix,
            "/".join([subdir + suffix for subdir in path_collection[0].split("/")[split_position:]])
        )
        files = [file + suffix for file in path_collection[2]]

        os.mkdir(root_path)
        for source, destination in zip(path_collection[2], files):
            if source in exclude:
                continue
            encrypt_file(os.path.join(path_collection[0], source), os.path.join(root_path, destination), fernet_object)

def decrypt_recursively(path: str, out_path: str, fernet_object: Fernet, suffix: str):
    """ Encrypts folders recursively """
    output_root_path = os.path.join(out_path, os.path.basename(path).replace(suffix, ""))
    output_prefix = os.path.split(output_root_path)[0]
    split_position = len(path.split("/")) - 1  # First item is empty because of path starting with /

    for path_collection in os.walk(path):
        root_path = os.path.join(
            output_prefix,
            "/".join([subdir.replace(suffix, "") for subdir in path_collection[0].split("/")[split_position:]])
        )
        files = [file.replace(suffix, "") for file in path_collection[2]]

        os.mkdir(root_path)
        for source, destination in zip(path_collection[2], files):
            decrypt_file(os.path.join(path_collection[0], source), os.path.join(root_path, destination), fernet_object)

def main(args: argparse.Namespace):
    """ Main function """
    # print(args)
    paths = args.path.split(",")
    excludes = args.exclude.split(",") if args.exclude is not None else []
    output = args.output if args.output is not None else os.getcwd()
    decrypt_key = base64.urlsafe_b64decode(args.decrypt.encode("utf-8")) if args.decrypt is not None else None
    suffix = args.suffix if args.suffix is not None else "-encrypted"

    print(f"\n\t\
Paths: {paths}\n\t\
Exclude: {excludes}\n\t\
Output Path: '{output}'\n\t\
Suffix: '{suffix}'\n\t\
Decrypt Key: {decrypt_key}\n")

    key = decrypt_key
    if decrypt_key:
        fernet_object = Fernet(decrypt_key)
    else:
        key = Fernet.generate_key()
        fernet_object = Fernet(key)

    for path in paths:
        if os.path.isdir(path):
            if decrypt_key:
                decrypt_recursively(path, output, fernet_object, suffix)
            elif decrypt_key is None:
                encrypt_recursively(path, output, fernet_object, suffix, excludes)

        elif os.path.isfile(path):
            base_name = os.path.basename(path)
            if decrypt_key:
                decrypt_file(path, os.path.join(output, base_name.replace(suffix, "")), fernet_object)
            elif decrypt_key is None:
                encrypt_file(path, os.path.join(output, base_name + suffix), fernet_object)

    print(f"This is your encryption key. Keep it safe.\n'{base64.urlsafe_b64encode(key).decode('utf-8')}'")
