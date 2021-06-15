import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='mentor',  
     version='0.1',
     scripts=['mentor'] ,
     author="Oscar Schmitt Kremer",
     author_email="oscar.s.kremer@hotmail.com",
     description="A package to simulate direct and inverse kinematics of Mentor Didactic Robotic Arm",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/oscarkremer/mentor",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )