from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Joel Duverge",
    author_email="joelduverge321@gmail.com",
    description="Snapshotalyzer 30000 is a tool to manage AWS EC2 instances, volumes and snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/joelduverge321/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    ''',
)
