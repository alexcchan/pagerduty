#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'pagerduty',
	version = '0.0.0',
	packages = ['pagerduty'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	url = 'https://github.com/alexcchan/pagerduty/tree/master',
	keywords = 'pagerduty api',
	description = 'PagerDuty API Wrapper for Python',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


