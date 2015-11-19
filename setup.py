"""
lookup
------

Look up words via the command line.

Links
`````

* `documentation <https://github.com/fengsp/lookup>`_
* `development version
  <http://github.com/fengsp/lookup/zipball/master#egg=lookup-dev>`_

"""
from setuptools import setup


setup(
    name='lookup',
    version='0.2',
    url='https://github.com/fengsp/lookup',
    license='BSD',
    author='Shipeng Feng',
    author_email='fsp261@gmail.com',
    description='Dictionary via the command line',
    long_description=__doc__,
    py_modules=['lookup'],
    zip_safe=False,
    platforms='any',
    entry_points={
        'console_scripts': [
            'lookup = lookup:command_line',
        ]
    },
    install_requires=[
        'pyquery',
        'requests'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
