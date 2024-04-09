from setuptools import setup, find_packages

setup(
    name='FactCheckLib',
    author='GONZO',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A Python library for fetching fact-checking data from Google Fact Check Explorer.',
    url='https://github.com/GONZOsint/factcheckexplorer',
    entry_points={
        'console_scripts': [
            'factchecklib = factchecklib:main'
        ]
    }
)
