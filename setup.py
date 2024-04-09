from setuptools import setup, find_packages

setup(
    name='FactCheckLib',
    author='GONZO',
    version="0.0.1",
    packages=find_packages(),
    url='https://github.com/GONZOsint/factcheckexplorer'
    install_requires=[
        'requests',
    ],
    description='A Python library for fetching fact-checking data from Google Fact Check Explorer.',
    url='https://github.com/GONZOsint/factcheckexplorer',
)
