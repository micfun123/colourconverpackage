from setuptools import setup, find_packages
 
VERSION = '0.0.1'
DESCRIPTION = "converts different colour formats. "

setup(
    name='colour_converter',
    version=VERSION,
    author='Michael Parker',
    author_email='your email',
    url='https://github.com/micfun123/colourconverpackage',
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages()
)

# python3 setup.py bdist_wheel
# twine upload dist/*
# sudo rm -rf ./build ./dist ./*egg-info