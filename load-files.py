#!/usr/bin/python

from requests import get
from os.path import basename
from os import mkdir
from shutil import rmtree

"""
Script to download files for Tabletop Simulator Workshop mod.

To use it you need to install some requirements:

```
pip install requests
```
"""

downloads_path = 'downloads'

urls = []
filepath = '681382159.json'

print('Reading data file {}'.format(filepath))

with open(filepath) as fin:
    for line in fin:
        urls.append(line.rstrip())

print('Found {} urls.'.format(len(urls)))

print('Removing duplications.')
urls = list(dict.fromkeys(urls))
print('{} urls remain after removing duplications.'.format(len(urls)))

print('Deleting downloads dir.')
rmtree(downloads_path, ignore_errors = True)

print('Create downloads dir.')
mkdir(downloads_path)

print('Downloading files:')
for url in urls:
    filename = '{}/{}'.format(downloads_path, basename(url))
    with open(filename, 'wb') as local_file:
        remote_file = get(url)
        local_file.write(remote_file.content)
        print('Wrote {} to {}.'.format(url, filename))
