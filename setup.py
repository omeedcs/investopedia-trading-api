from setuptools import setup, find_packages

setup(
  name = 'InvestopediaApiFixed',
  packages = ['InvestopediaApiFixed'],
  version = '1.2',
  description = 'An API for Investopedia\'s paper trading simulator (fixed by Omeed)',
  author = 'Kirk Thaker and Omeed Tehrani',
  author_email = 'omeed26@gmail.com',
  url = 'https://github.com/omeedcs/investopedia-trading-api.git',
  download_url = 'https://github.com/kirkthaker/investopedia-trading-api/archive/1.1.tar.gz',
  keywords = ['trading', 'finance', 'investopedia', 'algorithmic'],
  classifiers = [],
  install_requires=['mechanicalsoup'],
)
