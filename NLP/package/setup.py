import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name = 'textpreprocess_2022', # Should be unique globally
    version = '0.0.1',
    author = 'Nitin',
    email = 'portfolionitin.ai@gmail.com',
    description = 'This is text preprocessing package',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers = [
        'programming_language :: python :: 3',
        'license ::OSI Approved :: MIT Approvd',
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.6'
)