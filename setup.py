from setuptools import find_packages
from setuptools import setup

setup(
    name='morse-transcript',
    version='0.0.3',
    license='MIT',
    author='Gughanathan M',
    author_email='gugu.ap900@gmail.com',
    description='Convert text to Morse Code and vise-versa.',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    url='https://github.com/gugupy/morsecodetranslator',
    include_package_data=True,
    keywords=['MorseCode', 'Morse'],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    entry_points={
        'console_scripts': [
            'morse=cli.morse:main'
        ]
    },
)
