from setuptools import setup

setup(
    name='psapiApp',
    packages=['psapiApp'],
    include_packages_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
    ],
)