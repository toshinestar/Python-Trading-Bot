from setuptools import setup, find_packages

# load the README file.
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    # this will be my Library name.
    name='pyrobot',

    # Want to make sure people know who made it.
    author='Alex Reed',

    # also an email they can use to reach out.
    author_email='coding.sigma@gmail.com',

    # I'm in alpha development still, so a compliant version number is a1.
    # read this as MAJOR VERSION 0, MINOR VERSION 1, MAINTENANCE VERSION 0
    version='0.1.0',

    # here is a simple description of the library, this will appear when someone searches for the library on https://pypi.org/search
    description='A trading robot built for Python that uses the TD Ameritrade API.',

    # I have a long description but that will just be my README file, note the variable up above where I read the file.
    long_description=long_description,

    # want to make sure that I specify the long description as MARKDOWN.
    long_description_content_type="text/markdown",

    # here is the URL you can find the code, this is just the GitHub URL.
    url='https://github.com/areed1192/python-trading-robot',

    # there are some dependencies to use the library, so let's list them out.
    install_requires=[
        'websockets==8.0.2',
        'requests==2.22.0',
        'td-ameritrade-python-api==0.2.2'
    ],

    # some keywords for my library.
    keywords='finance, td ameritrade, api, trading robot',

    # here are the packages I want "build."
    packages=find_packages(include=['pyrobot'], exclude=['*config.py']),

    # I also have some package data, like photos and JSON files, so I want to include those too.
    include_package_data=True,

    # additional classifiers that give some characteristics about the package.
    classifiers=[

        # I want people to know it's still early stages.
        'Development Status :: 3 - Alpha',

        # My Intended audience is mostly those who understand finance.
        'Intended Audience :: Financial and Insurance Industry',

        # My License is MIT.
        'License :: OSI Approved :: MIT License',

        # I wrote the client in English
        'Natural Language :: English',

        # The client should work on all OS.
        'Operating System :: OS Independent',

        # The client is intendend for PYTHON 3
        'Programming Language :: Python :: 3'
    ],

    # you will need python 3.7 to use this libary.
    python_requires='>=3.7'

)
