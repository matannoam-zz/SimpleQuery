# SimpleQuery
query from containers of objects, in Python

## Query pattern

The Query pattern uses criteria on classes and fields to retrieve
value objects from a dataset. Those criteria are a field, an operator,
and a value. For example, ('last_name', =, 'Fowler') or ('price', <, 100.00).

## Setting up development environment
It is always recommended to use a virtual environment for each
Python appplication. Create the environment once, after cloning
this repository to your machine.
```
python3 -m venv .env
```

For each terminal session going forward, work on the virtual
environment and use its copy of python.
```
source .env/bin/activate
```

## Running tests
Tests are written in unittest syntax, so no additional package are needed
to run them
```
python -m unittest discover
```
