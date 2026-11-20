# pytest-click

[![Build](https://github.com/Stranger6667/pytest-click/actions/workflows/build.yml/badge.svg)](https://github.com/Stranger6667/pytest-click/actions/workflows/build.yml)
[![Coverage](https://codecov.io/github/Stranger6667/pytest-click/coverage.svg?branch=master)](https://codecov.io/github/Stranger6667/pytest-click?branch=master)
[![Version](https://img.shields.io/pypi/v/pytest-click.svg)](https://pypi.org/project/pytest-click/)
[![Python versions](https://img.shields.io/pypi/pyversions/pytest-click.svg)](https://pypi.org/project/pytest-click/)
[![License](https://img.shields.io/pypi/l/pytest-click.svg)](https://opensource.org/licenses/MIT)

[pytest](https://github.com/pytest-dev/pytest) plugin for [Click](https://click.palletsprojects.com/).

## Installation

```
pip install pytest-click
```

## Usage

`pytest-click` comes with two fixtures: `cli_runner` and `isolated_cli_runner`.

```python
import click


def test_cli(cli_runner):
    @click.command()
    @click.argument("name")
    def hello(name):
        click.echo(f"Hello {name}!")

    result = cli_runner.invoke(hello, ["Peter"])
    assert result.exit_code == 0
    assert result.output == "Hello Peter!\n"
```

`isolated_cli_runner` runs each test inside `CliRunner.isolated_filesystem()`:

```python
import click


def test_fixture(isolated_cli_runner):
    @click.command()
    @click.argument("f", type=click.File())
    def cat(f):
        click.echo(f.read())

    with open("hello.txt", "w") as f:
        f.write("Hello World!")

    result = isolated_cli_runner.invoke(cat, ["hello.txt"])
    assert result.exit_code == 0
    assert result.output == "Hello World!\n"
```

Both runners can be configured with the `runner_setup` mark:

```python
import pytest


@pytest.mark.runner_setup(charset="cp1251", env={"test": 1}, echo_stdin=True)
def test_runner_setup(cli_runner): ...
```

All kwargs are passed to `click.testing.CliRunner`.
