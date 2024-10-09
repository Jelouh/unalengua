import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

setup(
    name='unalengua',
    version='0.0.1',
    url='https://github.com/Jelouh/unalengua',
    license='MIT',
    author='Francisco Griman',
    author_email='grihardware@gmail.com',
    description='A simple library for Unalengua API.',
    long_description=(HERE / "README.md").read_text(encoding='utf-8'),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.32.3',
        'ua-generator==1.0.5'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12'
    ],
)