# python-project-template
Simple project template for Python projects.

This repository uses [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) to define some templates for python projects.

## Features
The project templates defined in this repository comes with the following tools:
- [poetry](https://python-poetry.org/): package dependecy management tool
- [pre-commit](https://pre-commit.com/): run pre-commit hooks 
- [pytest](https://docs.pytest.org/en/7.1.x/): easily write and run tests
- [sphinx](): tbd
- [ci/ci](): tbd
- logging: basic configuration for logging using the `logging` python package

## Usage

To set up a new project with this template, first you need to install `cookiecutter` (installation in a separate virtualenv is suggested):
```
pip install cookiecutter
```

Then, go to the folder where you want to put the new project and just run
```
cookiecutter git@github.com:mattiatantardini/python-project-template.git
```

You will be asked to choose among the available templates and some additional information (project name, project directory, etc.) to set up the project.

## Docs
You can find modere detailed documentation about this project, how to use this template and an explanation on the tools used in the [github pages](https://mattiatantardini.github.io/python-project-template/) of the repo.

## Contribution
Any comment, feedback and contribution is very welcomed! Please use the github issue tracker as a preferential way to give your contribution.
