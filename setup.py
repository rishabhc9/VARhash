from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='varhash',
  version='0.0.2',
  description='Implementation of VAR Hash in Python',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/rishabhc9',  
  author='Rishabh Chopda',
  author_email='aaditchopda2@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='varhash', 
  packages=find_packages(),
  install_requires=[''] 
)