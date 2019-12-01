from setuptools import setup, find_packages
from os import path


project_directory = path.abspath(path.dirname(__file__))


def load_from(file_name):
    with open(path.join(project_directory, file_name), encoding='utf-8') as f:
        return f.read()


setup(
    name='{{module_name}}',
    version=load_from('{{module_name}}/{{module_name}}.version').strip(),
    description='-- Fill description --',
    long_description=load_from('README.md'),
    long_description_content_type='text/markdown',
    url='-- Fill project url --',
    author='-- Fill author --',
    author_email='-- Fill email --',
    license='-- Fill license --',
    packages=find_packages(include=[
        '{{module_name}}',
    ]),
    package_data={
        '{{module_name}}': [
            '{{module_name}}.version',
        ]
    },
    test_suite='tests',
    install_requires=[
    ],
    classifiers=[
    ],
    keywords='-- Fill keywords -- ',
)
