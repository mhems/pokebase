import setuptools


def readme_text():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='pokebase',
    packages=['pokebase'],
    version='0.0.1',
    description='A Python wrapper for the pokebase wrapper of the PokeAPI database',
    long_description=readme_text(),
    long_description_content_type='text/markdown',
    author='Matt Hems',
    url='https://github.com/mhems/pokebase',
    keywords=['database', 'pokemon', 'wrapper'],
    install_requires=['requests'],
    license='BSD License',
    requires_python=">=3.8",
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ]
)
