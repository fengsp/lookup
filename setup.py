"""
lookup
------

Look up words via the command line.

Links
`````

* `documentation <https://github.com/fengsp/lookup>`_
* `development version
  <http://github.com/fengsp/lookup/zipball/master#egg=pypages-dev>`_

"""
from setuptools import setup


setup(
    name='lookup',
    version='0.1',
    url='https://github.com/fengsp/lookup',
    license='BSD',
    author='Shipeng Feng',
    author_email='fsp261@gmail.com',
    description='Dictionary via the command line',
    long_description=__doc__,
    py_modules=['lookup'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
