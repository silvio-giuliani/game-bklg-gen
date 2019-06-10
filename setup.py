from setuptools import setup

setup(
    name='generator',
    version=1.0,
    packages=['generator'],
    install_requires=['pytest'],
    entry_points={'console_scripts': ['generator = generator.__main__:main']}
)
