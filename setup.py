try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'GCore Scoreboard Generator',
    'author': 'Lord Bonaparte',
    'url': 'someurl',
    'download_url': 'someurl',
    'author_email': 'eesitmaarja@gmail.com',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['gcore'],
    'scripts': [],
    'name': 'gcore'
}

setup(**config)
