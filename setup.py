from distutils.core import setup
from setuptools import find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pyroaman',
    version='0.1.1',
    license='MIT',
    description='Roam Research with Python',
    author = 'Bruno Godefroy',
    author_email='brgo@mail.com',
    url = 'https://github.com/br-g/pyroaman',
    download_url = 'https://github.com/br-g/pyroaman/archive/v0.1.1.tar.gz',
    keywords = ['Roam Research'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.6',
    install_requires=[
        'cached_property',
        'dataclasses',
        'loguru',
        'tqdm',
        'pathlib',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
