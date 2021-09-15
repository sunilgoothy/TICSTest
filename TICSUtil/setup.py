from setuptools import setup, find_packages

setup(name='TICSUtil',
      version='0.0.14',
      description='This package is a library of small functions used in TICS development.',
      author='Sunil Goothy',
      author_email='sunil.goothy@tmeic.in',
      install_requires=[
        "getmac>=0.8.2",
        "cryptography>=2.9.2",
        "ipaddress>=1.0.23"
        ],
      packages=find_packages(),
    )
