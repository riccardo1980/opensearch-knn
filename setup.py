from setuptools import find_packages, setup

with open("requirements.txt", 'r') as f:
    REQUIREMENTS = f.read()

setup(
    name='simple_opensearch_knn',
    version="0.1",
    packages=find_packages(
        include=['simple_opensearch_knn', 'simple_opensearch_knn.*']
    ),
    install_requires=[i for i in REQUIREMENTS.split('\n') if i is not ""]
)
