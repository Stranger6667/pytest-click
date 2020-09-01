def test_fixture(testdir):
    testdir.makepyfile(
        """
    from click.testing import CliRunner

    def test_fixture(cli_runner):
        assert isinstance(cli_runner, CliRunner)
    """
    )
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines("test_fixture.py::test_fixture PASSED*")


def test_real_invocation(testdir):
    testdir.makepyfile(
        """
    import click

    def test_fixture(cli_runner):

        @click.command()
        @click.argument('name')
        def hello(name):
            click.echo('Hello %s!' % name)

        result = cli_runner.invoke(hello, ['Peter'])
        assert result.exit_code == 0
        assert result.output == 'Hello Peter!\\n'
    """
    )
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines("test_real_invocation.py::test_fixture PASSED*")


def test_runner_setup(testdir):
    testdir.makepyfile(
        """
    import pytest

    @pytest.mark.runner_setup(charset='cp1251', env={'test': 1}, echo_stdin=True)
    def test_runner_setup(cli_runner):
        assert cli_runner.charset == 'cp1251'
        assert cli_runner.env == {'test': 1}
        assert cli_runner.echo_stdin
    """
    )
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines("test_runner_setup.py::test_runner_setup PASSED*")


def test_docstring(testdir):
    result = testdir.runpytest("--fixtures")
    assert (
        "    Instance of `click.testing.CliRunner`. Can be "
        "configured with `@pytest.mark.runner_setup`." in result.stdout.lines
    )
