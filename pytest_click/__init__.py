# coding: utf-8
from .fixtures import cli_runner, isolated_cli_runner


__version__ = '0.2'


def pytest_configure(config):
    config.addinivalue_line(
        'markers', 'runner_setup(**kwargs): Pass kwargs to `click.testing.CliRunner` initialization.'
    )
