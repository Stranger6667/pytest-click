# coding: utf-8
import pytest
from click.testing import CliRunner


@pytest.fixture
def cli_runner(request):
    """
    Instance of `click.testing.CliRunner`. Can be configured with `@pytest.mark.runner_setup`

    @pytest.mark.runner_setup(charset='cp1251')
    def test_something(cli_runner):
        ...
    """
    init_kwargs = {}
    marker = request.node.get_closest_marker('runner_setup')
    if marker:
        init_kwargs = marker.kwargs
    return CliRunner(**init_kwargs)


@pytest.yield_fixture
def isolated_cli_runner(cli_runner):
    """
    Instance of `click.testing.CliRunner` with automagically `isolated_filesystem()` called.
    """
    with cli_runner.isolated_filesystem():
        yield cli_runner
