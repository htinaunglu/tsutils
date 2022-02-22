from distutils.core import setup
setup(
  name = 'tsautils',         # How you named your package folder (MyLib)
  packages = ['tsautils'],   # Chose the same as "name"
  version = '0.0.7',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Time Series Utilities',   # Give a short description about your library
  author = 'htinaunglu',                   # Type in your name
  author_email = 'htinaunglu@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/htinaunglu/tsutils/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/htinaunglu/tsutils.git',    # I explain this later on
  keywords = ['Utilities', 'LSTM', 'Time Series'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)