import re
from setuptools import setup, find_packages

module_file = open("endor/__init__.py").read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", module_file))
long_description = open('README.md').read()

setup(
    name='endor',
    description='API Rest APP unispan',
    packages=find_packages(),
    author='Unispan',
    author_email='devteam [at] unispan.com.pe',
    scripts=['bin/endor'],
    install_requires=[
                        'Click',
                        'PyYAML',
                        'waitress',
                        'falcon',
                        'colander',
                        'colanderalchemy',
                        'psycopg2',
                        'sqlalchemy==1.1.0',
                        'SQLAlchemy-Utils==0.29.2',
                        'dicttoxml==1.7.4',
                        'python-slugify==0.1.0'
                    ],
    version=metadata['version'],
    url='https://github.com/unispan/api.app.unispan',
    license="MIT",
    zip_safe=False,
    keywords="api, rest, unispan",
    long_description=long_description,
    classifiers=[
                    'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Topic :: Software Development :: Build Tools',
                    'Topic :: Software Development :: Libraries',
                    'Topic :: Software Development :: Testing',
                    'Topic :: Utilities',
                    'Operating System :: MacOS :: MacOS X',
                    'Operating System :: Microsoft :: Windows',
                    'Operating System :: POSIX',
                    'Programming Language :: Python :: 2.6',
                    'Programming Language :: Python :: 2.7',
                ]
)
