from setuptools import setup

setup(
    name='quying',
    version=5.0,
    packages=['quying'],
    install_requires=['argparse', 'requests'],
    entry_points={'console_scripts': ['quying = quying.cli.main:main']}
)
