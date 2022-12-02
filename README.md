# fastapi-template-service

<p align="center">
    <em>A template for FastAPI applications</em>
</p>

---

### About

**fastapi-template-service** is a base project for FastAPI applications.

The main purpose is to have a base code already working and it allows to you generate APIs faster than begin from scratch. It will require minimal changes for run yours new application based on your API's requirements .

---

### Prerequisites

If you want to run the project on Docker, first you should have some applications installed:

```bash
docker
docker-compose
Poetry
dbmate
```

```bash
pip install docker-compose
```

```bash
pip install poetry
```

---

## Run

### Docker


1. Start the application

```bash
make up
```

2. Stop the application
```bash
make down
```

### Local environment

1. Access your virtual environment:

```bash
poetry shell
```

2. Install the project dependencies:

```bash
poetry install
```

3. Don't forget to run the [migrations](#migrations) and start the project:

```bash
uvicorn app.main:app --reload
```

---

## Running the tests

### Local environment

```bash
pytest -v /tests
```

---

## Running the Pre-Commit tool

The project includes a development dependency called [Pre-Commit](https://pre-commit.com/) which is a framework for managing and maintaining pre-commit hooks like code linting. To initialize it on your machine, inside your virtual environment, you just have to do:

```bash
pre-commit install
```

---

## Doing commits with Commitizen

The project also have includes a development dependency called [Commitizen](https://commitizen-tools.github.io/commitizen/), this dependency helps us to make commits based on a defined standard by the team.

### Installation

Global installation

```bash
pip3 install Commitizen
```

macOS

On macOS, it can also be installed via homebrew:

```bash
brew install commitizen
```

### Usage

Run in your terminal

```bash
cz commit
```
## <a name="migrations"></a> Migrations

We use [DbMate](https://github.com/amacneil/dbmate), Refer to DBMate's documentation for any doubts on usage.

### Install dbmate

```bash
brew install dbmate
```

### New migration

to create a new migration just run

```bash
dbmate new <migration_name>
```

### Run migrations

to run all pending migrations type

```bash
dbmate up
```

---

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast, web framework for building APIs with Python 3.9+
- [PostgreSQL](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database
- [DbMate](https://github.com/amacneil/dbmate) - A lightweight, framework-agnostic database migration tool.

---
