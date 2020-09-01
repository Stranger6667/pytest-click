def test_fixture(testdir):
    testdir.makeconftest(
        """
    try:
        from mock import patch, Mock
    except ImportError:
        from unittest.mock import patch, Mock

    def pytest_configure(config):
        config.patched = patch('pytest_click.fixtures.CliRunner.isolated_filesystem')
        config.patched.start()

    def pytest_unconfigure(config):
        config.patched.stop()
    """
    )
    testdir.makepyfile(
        """
    from click.testing import CliRunner

    def test_fixture(isolated_cli_runner):
        assert isinstance(isolated_cli_runner, CliRunner)
        assert isolated_cli_runner.isolated_filesystem.called
    """
    )
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines("test_fixture.py::test_fixture PASSED*")


def test_real_invocation(testdir):
    testdir.makepyfile(
        """
    import click

    def test_fixture(isolated_cli_runner):

        @click.command()
        @click.argument('f', type=click.File())
        def cat(f):
            click.echo(f.read())

        with open('hello.txt', 'w') as f:
            f.write('Hello World!')

        result = isolated_cli_runner.invoke(cat, ['hello.txt'])
        assert result.exit_code == 0
        assert result.output == 'Hello World!\\n'
    """
    )
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines("test_real_invocation.py::test_fixture PASSED*")


def test_docstring(testdir):
    result = testdir.runpytest("--fixtures")
    assert (
        "    Instance of `click.testing.CliRunner` with "
        "automagically `isolated_filesystem()` called." in result.stdout.lines
    )
