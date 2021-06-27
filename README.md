##Excerise Task
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: black](https://img.shields.io/badge/code%20style-Flake8-green)](https://github.com/PyCQA/flake8)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![security: bandit](https://img.shields.io/badge/security-safety-yellow)](https://github.com/pyupio/safety)


[![](App/tests/results/coverage.svg)]()

[comment]: <> (<br>coverage badge will appear after running tests :&#41;<br>)

[comment]: <> (P.S coverage 100%)

## Table of content

 - Technology stack
 - Quality Assurance
 - Installation
 - Running service
 - Test
 - Before commit
 - What I would do if had more time

## Technology Stack

 - Python 3.9
 - FastAPI 0.63
 - Redis 6
 - Locust performance tests
 - coverage.py + pytest

## Quality Assurance
##### Swagger documentation:
 - http://127.0.0.1:8000/docs
##### Clean Code:
 - Black, Flake8
 - isort: import sorting
 - Pre-commit: hooks for big files etc.
##### Security :
 - bandit: any left credential or AWS key
 - safety: any known package vulnerability



## Installation

Type in cmd
```
$ git clone https://github.com/RadoslawKzm/Excerise_Task.git
$ pip3 install -r requirements.txt
```

## Running the service

##### Docker start & build:
Starting services `$ docker-compose up --build app && docker-compose rm -fsv`
Stopping services:`$ docker-compose down` or crtl+c
##### Curl Testing
- Post request:
```
curl --location --request POST 'http://localhost:8000/ping' \
--header 'Content-Type: application/json' \
--data-raw '{"url": "https://google.com"}'
```
- Get request:
```
curl --location --request GET 'http://localhost:8000/info'
```
if above don't work try replacing localhost > 127.0.0.1


## Before commit
Steps to take before commit or your commit will not be accepted.<br>
- once at start if not done already `$ pip3 install -r requirements.txt`
- having main folder requirements installed `$ pre-commit run --all-files`

Before you send the code to the server, please runt this tests
```
$ python -m black --check -l 120 --exclude=venv .
$ python -m flake8 .
$ python -m isort --check-only --diff .
$ bandit -r ./App/
$ safety check --full-report
```
Part of errors you can fix running:
```
$ python -m black -l 120 --exclude=venv .
$ python -m isort .
```
