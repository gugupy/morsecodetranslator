from setuptools import find_packages
from setuptools import setup


setup(
    name='morcecodetranslator',
    version='1.0.1',
    license='MIT',
    author='Gughanathan M',
    author_email='gugu.ap900@gmail.com',
    description='Convert text to Morce Code',
    package_dir={'':'src'},
    packages=find_packages(where='src'),
    url='https://github.com/gugupy/morcecodetranslator',
    include_package_data=True,
    keywords='Morce Code',
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
