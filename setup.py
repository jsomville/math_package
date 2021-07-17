from setuptools import setup, find_packages

VERSION = '0.0.5' 
DESCRIPTION = 'Basic Math library'
LONG_DESCRIPTION = 'Basic Math library used to get familiar with the package and modules creation and management'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="jsbmath", 
        version=VERSION,
        author="JSB",
        author_email="email@domain.com",
        url="https://github.com/jsomville/math_package",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['singleton3'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
        ]
) 
