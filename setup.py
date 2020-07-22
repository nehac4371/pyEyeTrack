from distutils.core import setup

install_requires = []

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'PyEyeTrack',         
  packages = ['PyEyeTrack'],   
  version = '0.3.4',      
  license='MIT',        
  description = """PyEyeTrack is a python-based pupil-tracking library. The library tracks eyes with the commodity webcam 
                and gives a real-time stream of eye coordinates. It provides the functionality of eye-tracking and 
                blink detection and encapsulates these in a generic interface that allows clients to use these 
                functionalities in a variety of use-cases.""", 
  long_description=long_description,
  long_description_content_type="text/markdown",  
  authors = 'Kanchan Sarolkar, Kimaya Badhe, Neha Chaudhari, Samruddhi Kanhed and Shrirang Karandikar',                   
  author_email = 'pytracklibrary@gmail.com',      
  url = 'https://github.com/algoasylum/PyEyeTrack',  
  download_url = 'https://github.com/algoasylum/pyEyeTrack/archive/v_03_4.tar.gz',    
  keywords = ['Eye Tracking','blink detection','User Interface','Webcamera'], 
  install_requires=[
  'dlib==19.4',
  'keyboard==0.13.3=pypi_0',
  'numpy==1.18.1=pypi_0',
  'opencv==3.3.1',
  'pandas==0.24.0',
  'pyaudio==0.2.11',
  'pyqt==5.6.0',
  ],  
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
)