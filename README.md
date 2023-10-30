### Hexlet tests and linter status:
[![Actions Status](https://github.com/despiqqqq/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/despiqqqq/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9ec6da9ee736e21cec66/maintainability)](https://codeclimate.com/github/despiqqqq/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9ec6da9ee736e21cec66/test_coverage)](https://codeclimate.com/github/despiqqqq/python-project-50/test_coverage)
# Difference generator

### Performs comparison of documents in *.json, *.yml, *.yaml formats containing a dictionary of dictionaries. Finds differences in keys and their values and displays them in the specified format.

### You can either use the python package or call it from the command line.





##  Output formats

* stylish - used by default. Outputs the result as a multi-line text with a dictionary tree structure.
* plain - Outputs the result as a multiline text in the form:
  * Property ... was added ...
  * Property ... was removed ...
  * Property ... was updated ...
* json - Outputs the result as a json object.


## Installing and uninstalling a package:

* mmake build - package assembly.
* make package-install - package installation.
* make package-uninstal-hc - Removing a package. Including the package's built-in folder.


## Package options:
* -h, --help - show this help message and exit.
* -f, --format - possibility to specify the choice of format. See above for possible formats.


# Work difference generator
[![asciicast](https://asciinema.org/a/BJNNFxIBQCwyxQS2we8eqhK6N.svg)](https://asciinema.org/a/BJNNFxIBQCwyxQS2we8eqhK6N)