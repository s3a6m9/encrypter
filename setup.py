""" Setup File """
from setuptools import setup, find_packages

setup(
    name='encrypter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography'
    ],
    author='s3a6m9',
    description='A simple file encryption tool',
    url='https://github.com/s3a6m9/encrypter',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'encrypter=encrypter:main',
        ],
    },
)
