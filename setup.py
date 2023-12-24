from setuptools import setup, find_packages

setup(
    name='OCPIPyBridge',
    version='0.1.0',
    packages=find_packages(),
    description='Python library for Open Charge Point Interface (OCPI) protocol',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Chinmoy Bhuyan',
    author_email='dikibhuyan@gmail.com',
    url='https://github.com/hyndex/OCPIPyBridge',
    license='MIT',
    install_requires=[
        'pydantic>=1.8.2',
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
