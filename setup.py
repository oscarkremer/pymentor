from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='mentor',  
     version='0.1',
     scripts=['mentor/mentor.py', 'mentor/error.py'] ,
     author="Oscar Schmitt Kremer",
     author_email="oscar.s.kremer@hotmail.com",
     description="A package to implement a computational model of Mentor didactic robotic arm.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/oscarkremer/mentor",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
    install_requires=[
        'numpy',
        'pytest'
    ]
)