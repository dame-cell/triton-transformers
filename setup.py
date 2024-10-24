from setuptools import setup, find_packages

setup(
  name = 'triformer',
  packages = find_packages(),
  version = '0.0.1',
  license='MIT',
  description = 'Transformer components in Triton',
  author = 'Dame rajee',
  author_email = 'doss72180@gmail.com',
  url = 'https://github.com/dame-cell/Triformer/tree/mainr',
  keywords = [
    'artificial intelligence',
    'transformers'
    'deep learning'
  ],
  install_requires=[
    
    'torch>=2.2.1',
    'triton>=2.2.0'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)