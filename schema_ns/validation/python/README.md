
# Validation Code #

## Code ##
### ./tests ###

* Set of focused python unit tests; one for each syntax element.
    * executes the Test plan cases for that element
* Rich Instance Tests
    * examples of more complex cases
* VOTable Test
    * obsolete: exercising various linkage plans to VOTable

### ./utils ###

* utility modules used in testing.

## Requirements ##
Python Modules:
* json
* logging
* numpy
* os
* pytest
* re
* ssl
* sys
* unittest
* urllib
* xmlschema >= v1.1.2

## Usage ##
From command line:
```
  %>cd <base>/schema/validation/python
  %>pytest --log-file=<logfile> ./tests
```
