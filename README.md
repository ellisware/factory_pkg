[![Travis CI](https://travis-ci.org/ellisware/factory_pkg.svg?branch=master)](https://travis-ci.org/ellisware/factory_pkg)

# factory_pkg

Factory_pkg is a python package that simplifies data reading from the FANUC FIELD System common data model.  The package allows data access through python based object oriented programming instead of the more generic and cumbersome relational(OAS) REST-API. 

Python is an excellent tool for processing the large amounts of data collected in the edge based FIELD platform.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites


```
Python 3.6 (Anaconda Recommended)
```

### Installing

With large portions of the REST-API still to be covered, the package is only available as source code currently.  The source code will be installed in debug mode so that changes made to the package are reflected in its usage.

Download the Package or clone the repository. (Optionally create a new environment before downloading and installing)

```
git clone https://github.com/ellisware/factory_pkg
```

Change to the root directory of the package (where setup.py is located)

```
cd factory_pkg 
``` 

Run pip to install the package in debug mode using the specification in setup.py.

```
pip install -e
``` 




Once the package is installed it can be used by importing the library.

example.py:
```
from factory_pkg import site
```

The first step is to retrieve the site information which is used to identify the factory hierarchy.

example.py:
```
…
factory = site.Site() # for default xa-site
factory = site.Site("192.168.99.101:40001/v1") # for dev vm at 192.168.99.101
…
```

Then the node information can be used. 

example.py:
```
…
for controller in factory.nodes():
	print(controller.controller_id())
…
```

## Design Notes

Additionally, the package uses the [Lazy Initialization](https://en.wikipedia.org/wiki/Lazy_initialization#Python) design pattern to improve effeciency and responsivness to the end user.  Additionally, the package uses the [Facade](https://en.wikipedia.org/wiki/Facade_pattern#Python) design pattern to aggregate the underlying REST-API data.  

Much of this code base is contrary to the python principles of flat, beautiful code.  This is due to the underlying class representation of the FIELD api.  The FIELD class representation works very well for the relational data it represents.  The goal of this abstraction then includes allowing software to consume the package in a very pythonic way.

## Running the tests

All unit tests are located under the tests directory. Simply navigate to each directory and run test.py for that test.


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details and the process for submitting pull requests to us.


## Authors

* **Mike Ellis** - *Initial work* - [Other repositories](https://github.com/ellisware.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


