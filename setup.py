from setuptools import setup, find_packages

__author__ = 'valeriy.ilihmetov'


setup(
    name='oauthio-python',
    packages=['oauthio_python'],
    version='0.1',
    description='OAuth.io backend authorisation',
    author_email='ilikhmetov@gmail.com',
    url='https://github.com',
    download_url='https://github.com',
    keywords=['oauthio', 'oauthd'],
    classifiers=[],
    packages=find_packages(),
    install_requires=['requests>=2.8.0'],
)
