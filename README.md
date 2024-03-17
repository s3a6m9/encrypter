# Encrypter
Encrypts files/direcotires with a key using the python cryptography package.

Encrypter is a Python package designed to encrypt or decrypt files and folders. It provides a simple command-line interface for performing encryption and decryption tasks.

## Installation

To install Encrypter, you can use pip. If you're installing from this Git repository, use the following command:
```bash
pip install git+https://github.com/s3a6m9/encrypter.git
```

## Usage
> [!NOTE]  
> The encryption key is printed after the files are encrypted. This program does not delete the original files.

- `-h, --help`: Show the help message and exit.
- `--exclude`: Comma-separated list of files to exclude.
- `--output`: Output directory for encrypted files/folders.
- `--decrypt`: Add decryption key to decrypt file(s).
- `--suffix`: Add a suffix to decrypt/encrypt paths with.
- `path`: Path to the file/folder.

## Example

### Encrypting
Single file example that outputs the file in the same pwd directory with the suffix "-test_encrypt" (default is "-encrypted").
```bash
python3 -m encrypter /path/to/file.txt --suffix=-test_encrypt
```

### Decrypting
```bash
python3 -m encrypter /path/to/file.txt-test_encrypt --suffix=-test_encrypt --decrypt "your key"
```

## To do

- Add file/directory name encryption
- Allow folders to be excluded
- Encrypt with a pre-generated key passed through --encrypt
