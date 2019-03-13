from setuptools import setup, find_packages

setup(
    name='TFS',  # Required
    version='0.0.4',  # Required
    author="Paulo Sergio dos Santo Junior",
    author_email="paulossjuniort@gmail.com",
    description="Wrapper para acessar as informações do TFS",
    url="https://github.com/paulossjunior/tfs",
    packages=find_packages(),
    install_requires=['vsts','requestx'], 
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    setup_requires=['wheel'],
)