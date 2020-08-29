pytest-click
============

|Build| |Coverage| |Version| |Python versions| |License|

`pytest <https://github.com/pytest-dev/pytest>`_ plugin for `Click <http://click.pocoo.org/>`_.

Installation
------------

The current stable release:

::

    pip install pytest_click

Usage
-----

```pytest-click`` comes with some configurable fixtures - ``cli_runner`` and ``isolated_cli_runner``.

.. code:: python

    import click


    def test_cli(cli_runner):
        @click.command()
        @click.argument("name")
        def hello(name):
            click.echo("Hello %s!" % name)

        result = cli_runner.invoke(hello, ["Peter"])
        assert result.exit_code == 0
        assert result.output == "Hello Peter!\n"

.. code:: python

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

Both runners can be configured via ``runner_setup`` mark:

.. code:: python

    import pytest


    @pytest.mark.runner_setup(charset="cp1251", env={"test": 1}, echo_stdin=True)
    def test_runner_setup(cli_runner):
        ...

All kwargs will be passed to ``click.testing.CliRunner`` initialization.


.. |Build| image:: https://github.com/Stranger6667/pytest-click/workflows/build/badge.svg
   :target: https://github.com/Stranger6667/pytest-click/actions
.. |Coverage| image:: https://codecov.io/github/Stranger6667/pytest-click/coverage.svg?branch=master
    :target: https://codecov.io/github/Stranger6667/pytest-click?branch=master
.. |Version| image:: https://img.shields.io/pypi/v/pytest-click.svg
   :target: https://pypi.org/project/pytest-click/
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/pytest-click.svg
   :target: https://pypi.org/project/pytest-click/
.. |License| image:: https://img.shields.io/pypi/l/pytest-click.svg
   :target: https://opensource.org/licenses/MIT
