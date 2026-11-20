import pytest

from .fixtures import cli_runner, isolated_cli_runner

__all__ = ["cli_runner", "isolated_cli_runner"]
__version__ = "2.0.0"


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "runner_setup(**kwargs): Pass kwargs to `click.testing.CliRunner` initialization.",
    )
