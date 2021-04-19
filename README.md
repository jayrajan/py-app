# py-app - A simple Time Logging App

[![Documentation Status](https://readthedocs.org/projects/randomdataset/badge/?version=latest)](https://randomdataset.readthedocs.io/en/latest/?badge=latest)
[![Testing](https://github.com/ericspod/RandomDataset/workflows/Unittests/badge.svg)](https://github.com/ericspod/RandomDataset/actions)
[![codecov](https://codecov.io/gh/ericspod/RandomDataset/branch/master/graph/badge.svg)](https://codecov.io/gh/ericspod/RandomDataset)

## Description
This repository contains the simple library for managing time logging app built using Python3 with basic CI/CD integration and tools.

### This is a python based app that can:
- allow users to enter their weekly/daily work hours
- save the data in an external database
- Display the information graphically or as as a dashboard.


### Core Features

- Frontend - GUI where the user can interact with the app
- Backend - database which handles the data
- Control code which handles requests between user and the database.


Install this library from a git clone:

```bash
$ pip install .
```

Data is generated from a YAML schema describing the names of tables/datasets and the fields they have. The YAML file
consists of a sequence of dictionaries used to instantiate objects from the library or from other libraries present
in the Python path. This allows custom code to be injected into the generation process.

An example schema is used to generate a list of customer records in `customerschema.yaml`:

```yaml
- typename: randomdataset.generators.CSVGenerator
  num_lines: 10
  dataset:
    name: customers
    typename: randomdataset.Dataset
    fields:
    - name: id
      typename: randomdataset.UIDFieldGen
    - name: FirstName
      typename: randomdataset.StrFieldGen
      lmin: 6
      lmax: 14
    - name: LastName
      typename: randomdataset.StrFieldGen
      lmin: 6
      lmax: 14
```
Generates random datasets for testing and fun.

This repository contains a simple library for generating random tabular datasets of virtually any size. It also serves
as an example repository for a Python code base with basic CI/CD integration and tools.
This will create a single dataset "customers" stored in a CSV file `customers.csv`. This file is geneated by invoking
the included command:

```bash
$ generate_dataset customerschema.yaml .
```

This generates the `customers.csv` file:

```csv
id,FirstName,LastName
0,"QDFFgv4XBd5VW","O1Odro"
1,"Gp4mYq","82IPIChjBALg"
2,"LR7KVudB","HcAPBwM"
3,"6FfWGEYS0Q","5NbspSBJk"
4,"si1Tj0xSBB2","eChYKAaW5aa8R"
5,"DYP6OMerUUFOR","pYNXUTNLqdrv"
6,"ltfnhTgrJF","2Rctye"
7,"1tAoaDl57Lo5","xMkVKt6O"
8,"1yJImoqiwf","IJICD8W6B8k"
9,"XkYgS7","8owHyjR"
```

## Repository Setup

A relatively simple set of features which link into the code are set up on this repo to ensure good coding practice:

* Automatic documentation generation is done using ReadTheDocs, see [README.md](./docs/README.md)
* CI/CD implemented as flake8 and unit test execution using Github Actions, see [python-app.yml](./.github/workflows/python-app.yml)
* Code coverage is displayed using Codecov

Both ReadTheDocs and Codecov are integrated with the repo as webhooks. These can be setup through their respective sites
which require Github credentials to link with repos.

This repo mostly follows [GitFlow](http://datasift.github.io/gitflow/IntroducingGitFlow.html) with a `master` branch which is always
the current release of the code, and a `dev` branch that is the development version of the code.
Branch protection rules are in place for `master` which ensure that code can only be committed to the branch through reviewed PRs:

* Require pull request reviews before merging
* Require status checks to pass before merging ("build" action selected)
* Require branches to be up to date before merging
* Require linear history
* Include administrators
