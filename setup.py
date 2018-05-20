from setuptools import setup, find_packages
import sys
sys.path.append('./src')
sys.path.append('./tests')

setup(
    name='passwdgen',
    packages=find_packages(exclude=('tests')),
    test_suite='tests'
)
