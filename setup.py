from setuptools import setup

setup(
    name='readability_cli',
    version='0.1',
    py_modules=['readability_cli'],
    packages=['readability_cli'],
    install_requires=[
        'click==7.1.2',
        'readability-lxml==0.8.1',
        'requests==2.24.0',
        'html2text==2020.1.16'
    ],
    entry_points='''
        [console_scripts]
        readcli=readability_cli.app:cli
    ''',
)
