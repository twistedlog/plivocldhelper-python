from setuptools import setup
import sys

requires = ['requests']
if sys.version_info < (2, 6):
    requires.append('simplejson')

setup(
    name = "plivocldhelper",
    py_modules = ['plivocldhelper'],
    version = "0.1",
    description = "Plivo Cld API client and RESTXML generator",
    author = "Plivo Team",
    author_email = "hello@plivo.com",
    url = "https://github.com/plivo/plivocldhelper-python",
    keywords = ["plivo", "rest"],
    install_requires = requires,
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony"
        ],
    long_description = """\
        Python Plivo Client Helper Library
         """ )
