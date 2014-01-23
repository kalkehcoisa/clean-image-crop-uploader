__author__ = 'Jayme Tosi Neto'

from distutils.core import setup
from setuptools import setup, find_packages

setup(name = "py-clean-image-crop-uploader",
    version = "0.0.1",
    description = "PyClean Image Crop Uploader (CICU) provides AJAX file upload and image CROP functionalities using pure python. It uses Modal from twitter-bootstrap. This is a fork of clean-image-crop-uploader.",
    long_description=open('README.rst').read(),
    author = "kalkehcoisa",
    author_email = "kalkehcoisa@gmail.com",
    url = "",
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        'Pillow>=1.5',
        'deform>=2.0a2',
        'colander>=1.0b1'
        ],
    classifiers = [
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: None',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
