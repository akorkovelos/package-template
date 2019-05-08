from distutils.core import setup

import gons_test

long_description = """
Short description...
"""

setup(
    name='gons_test',
    version=gons_test.__version__,
    author='test',
    author_email='test',
    description='test',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='test_repo_lonk',
    packages=['gons_test'],
    install_requires=[
        'backcall==0.1.0',
        'colorama==0.4.1',
        'decorator==4.4.0',
        'et-xmlfile==1.0.1',
        'ipython==7.5.0',
        'ipython-genutils==0.2.0',
        'jdcal==1.4.1',
        'jedi==0.13.3',
        'numpy==1.16.3',
        'openpyxl==2.6.2',
        'pandas==0.24.2',
        'parso==0.4.0',
        'pickleshare==0.7.5',
        'prompt-toolkit==2.0.9',
        'Pygments==2.3.1',
        'python-dateutil==2.8.0',
        'pytz==2019.1',
        'six==1.12.0',
        'traitlets==4.3.2',
        'wcwidth==0.1.7'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)