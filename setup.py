from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='FactCheckLib',
    author='GONZO',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A Python library for fetching fact-checking data from Google Fact Check Explorer.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/GONZOsint/factcheckexplorer',
)
