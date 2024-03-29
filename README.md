# Poetry Dotenv Plugin

[![CI](https://github.com/mpeteuil/poetry-dotenv-plugin/actions/workflows/build.yml/badge.svg)](https://github.com/mpeteuil/poetry-dotenv-plugin/actions/workflows/build.yml)

A [Poetry](https://python-poetry.org/) plugin that automatically loads environment variables from `.env` files into the environment before poetry commands are run.

Supports Python 3.7+[^1]

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
poetry self add poetry-dotenv-plugin
```

### Coming from Pipenv

If you are transitioning from `pipenv` there shouldn't be much to change with regard to the `.env` loading. If you were a user of [`pipenv`'s environment variables](https://pipenv.pypa.io/en/latest/advanced/#automatic-loading-of-env) to control `.env` loading then you can use the analogous environment variables listed below.

Pipenv env var | Poetry env var
-------------- | ----------------------
PIPENV_DOTENV_LOCATION | POETRY_DOTENV_LOCATION
PIPENV_DONT_LOAD_ENV | POETRY_DONT_LOAD_ENV

### Overriding existing environment variables

By default, this plugin will override existing environment variables. This is because this plugin was built to make onboarding for users coming from `pipenv` as seamless as possible. If you want to prevent existing environment variables from being overridden, you can set the `POETRY_DOTENV_DONT_OVERRIDE` environment variable to `true`.[^2]

[^1]: Python 3.7 is supported only when using Poetry < [1.6.0](https://python-poetry.org/history/#160---2023-08-20), which [dropped support for Python 3.7](https://github.com/python-poetry/poetry/pull/7674).
[^2]: See [#16](https://github.com/mpeteuil/poetry-dotenv-plugin/pull/16) for background.
