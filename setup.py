from setuptools import setup, find_packages

setup(
    name='rfc-parsers',
    version='0.1',
    description='Parsers for grammars defined in various RFCs',
    url='https://github.com/lanzz/rfc-parsers',
    license='MIT',
    keywords='rfc parser',
    author='Mihail Milushev',
    author_email='mihail.milushev@lanzz.org',

    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'abnf == 0.1',
    ],
    dependency_links=[
        'git+https://github.com/lanzz/abnf#egg=abnf-0.1',
    ],
)
