from setuptools import setup


setup(
    name='segmented',
    version='1.0',
    url='https://github.com/thewarsawpakt/flask-segmented',
    license='BSD',
    author='thewarsawpakt',
    author_email='plexxious@outlook.com',
    description='Access control',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    package_dir={'': 'src'},
    packages=['segmented']
)
