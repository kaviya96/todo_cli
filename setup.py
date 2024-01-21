from setuptools import setup
setup(
    name = 'todo',
    version = '0.1.0',
    packages = ['todo'],
    install_requires = ['requests','pytest'], 
    entry_points = {
        'console_scripts': [
            'todo = todo.__main__:main'
        ]
    })