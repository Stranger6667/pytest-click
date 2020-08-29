from _pytest.config import Config

from .fixtures import cli_runner, isolated_cli_runner


def pytest_configure(config: Config) -> None:
    config.addinivalue_line(
        "markers",
        "runner_setup(**kwargs): Pass kwargs to `click.testing.CliRunner` initialization.",
    )
