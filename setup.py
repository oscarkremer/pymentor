import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='mentor',  
     version='0.1',
     scripts=['mentor/mentor.py', 'mentor/error.py'] ,
     author="Oscar Schmitt Kremer",
     author_email="oscar.s.kremer@hotmail.com",
     description="A package to implement a physical model of the Mentor \\
     didactic robotic arm. The package includes of direct and inverse kinematics.',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/oscarkremer/mentor",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    install_requires=[
        'itertools',
        'numpy',
        'pytest'
    ]
)