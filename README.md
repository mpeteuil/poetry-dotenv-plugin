# Poetry Dotenv Plugin

A [Poetry](https://python-poetry.org/) plugin that automatically loads environment variables from `.env` files into the environment before poetry commands are run.

Supports Python 3.6+

```sh
$ cat .env
MY_ENV_VAR='Hello World'

$ poetry run python -c 'import os; print(os.environ.get("MY_ENV_VAR"))'
Hello World
```

This plugin depends on the [`python-dotenv` package](https://github.com/theskumar/python-dotenv) for its functionality and therefore also supports features that `python-dotenv` supports. Interpolating variables using POSIX variable expansion for example.

### Origins

Initial implementation based on the event handler application plugin example in the [Poetry docs](https://python-poetry.org/docs/plugins/#event-handler).

## Install

```sh
poetry plugin add poetry-dotenv-plugin
```

### Coming from Pipenv

If you are transitioning from `pipenv` there shouldn't be much to change with regard to the `.env` loading. If you were a user of [`pipenv`'s environment variables](https://pipenv.pypa.io/en/latest/advanced/#automatic-loading-of-env) to control `.env` loading then you can use the analogous environment variables listed below.

Pipenv env var | Poetry env var
-------------- | ----------------------
PIPENV_DOTENV_LOCATION | POETRY_DOTENV_LOCATION
PIPENV_DONT_LOAD_ENV | POETRY_DONT_LOAD_ENV
