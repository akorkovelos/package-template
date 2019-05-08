import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

long_description = """
Short description...
"""

setuptools.setup(
    name='gons_test',
    version='1.0.3',
    author='Alexandros Korkovelos',
    author_email='alekor@desa.kth.se',
    description='This is a test package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alekordESA/gonset-example',
    packages=['gons_test'],
    install_requires=[
        'backcall>=0.1',
        'colorama>=0.4',
        'decorator>=4.4',
        'et-xmlfile>=1.0',
        'ipython>=7.5',
        'ipython-genutils>=0.2',
        'jdcal>=1.4',
        'jedi>=0.13',
        'numpy>=1.16',
        'openpyxl>=2.6',
        'pandas>=0.24',
        'parso>=0.4',
        'pickleshare>=0.7',
        'prompt-toolkit>=2.0',
        'Pygments>=2.3',
        'python-dateutil>=2.8',
        'pytz>=2019.1',
        'six>=1.12',
        'traitlets>=4.3',
        'wcwidth>=0.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)