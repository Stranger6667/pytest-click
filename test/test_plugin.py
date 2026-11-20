def test_markers(pytester):
    result = pytester.runpytest("--markers")
    assert (
        "@pytest.mark.runner_setup(**kwargs): "
        "Pass kwargs to `click.testing.CliRunner` initialization." in result.stdout.lines
    )
