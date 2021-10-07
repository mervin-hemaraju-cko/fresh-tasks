from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as rm:
    long_description = rm.read()

setup(
    name="freshtasks",
    version="1.0",
    author="Mervin Hemaraju",
    author_email="mervin.hemaraju@checkout.com",
    description="Fresh Task is a Python package that fetches a list of tasks from Fresh Service tickets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mervin-hemaraju-cko/fresh-tasks",
    packages=find_packages(exclude=('tests')),
    install_requires=[
          'requests'
      ],
    test_suite="tests",
    python_requires=">=3.7",
)