from setuptools import setup, find_packages


# Read the contents of your README file
with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name='OCPIPyBridge',
    version='0.1.4',
    packages=find_packages(),
    description='Python library for Open Charge Point Interface (OCPI) protocol',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Chinmoy Bhuyan',
    author_email='dikibhuyan@gmail.com',
    url='https://github.com/hyndex/OCPIPyBridge',
    license='MIT',
    install_requires=[
        'pydantic>=1.8.2',
        'typing-extensions>=3.7.4.3', 
        'httpx>=0.18.2'  # or other dependencies
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
