from distutils.core import setup

setup(
    name='GCore',
    version='0.0.1',
    author='Bonaparte',
    author_email='eestimaarja@gmail.com',
    packages=['gcore', 'gcore.generator', 'gcore.parser'],
    scripts=[],
    url='',
    license='',
    description='Scoreboard Generator',
    long_description=open('README.md').read()
)