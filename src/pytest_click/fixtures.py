# pylint: disable=redefined-outer-name
from typing import Generator

import pytest
from _pytest.fixtures import SubRequest
from click.testing import CliRunner


@pytest.fixture
def cli_runner(request: SubRequest) -> CliRunner:
    """Instance of `click.testing.CliRunner`. Can be configured with `@pytest.mark.runner_setup`.

    @pytest.mark.runner_setup(charset="cp1251")
    def test_something(cli_runner):
        ...
    """
    init_kwargs = {}
    marker = request.node.get_closest_marker("runner_setup")
    if marker:
        init_kwargs = marker.kwargs
    return CliRunner(**init_kwargs)


@pytest.fixture
def isolated_cli_runner(cli_runner: CliRunner) -> Generator[CliRunner, None, None]:
    """Instance of `click.testing.CliRunner` with automagically `isolated_filesystem()` called."""
    with cli_runner.isolated_filesystem():
        yield cli_runner
