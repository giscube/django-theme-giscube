from distutils.core import setup
from setuptools import find_packages


VERSION = '0.1'

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Environment :: Web Environment',
    'Development Status :: 5 - Production/Stable',
]

setup(
    name='django-theme-giscube',
    description='GISCube theme for the Django Admin',
    version=VERSION,
    author='Manel Clos',
    author_email='manelclos@gmail.com',
    license='BSD License',
    platforms=['OS Independent'],
    url='http://github.com/giscube/django-theme-giscube',
    packages=find_packages(exclude=['__pycache__']),
    include_package_data=True,
    classifiers=CLASSIFIERS,
    zip_safe=False,
)
