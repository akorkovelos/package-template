import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

long_description = """
Short description...
"""

setuptools.setup(
    name='test_package_kthdesa',
    version='1.0.0',
    author='Alexandros Korkovelos',
    author_email='alekor@desa.kth.se',
    description='This is a test package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alekordESA/package-template',
    packages=['test_package_kthdesa'],
    install_requires=[
        'numpy>=1.16',
        'pandas>=0.24'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)