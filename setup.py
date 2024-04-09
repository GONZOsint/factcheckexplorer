from setuptools import setup, find_packages

setup(
    name='FactCheckLib',
    author='GONZO',
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A Python library for fetching fact-checking data from Google Fact Check Explorer.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GONZOsint/factcheckexplorer',
)
