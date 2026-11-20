# Contributing to pytest-click

## Report bugs

Report bugs in the [issue tracker](https://github.com/Stranger6667/pytest-click/issues). Please include:

- the steps that reproduce the problem;
- what you expected and what happened instead;
- Python, pytest, Click and pytest-click versions.

A failing test that demonstrates the problem is very welcome.

## Pull requests

1. Fork the repository and target the `master` branch.
2. Install the [prek](https://prek.j178.dev) hooks: `prek install -t pre-commit -t commit-msg`.
3. Run the tests with tox, for example `tox -e py314`.
4. Add an entry under `Unreleased` in `CHANGELOG.md` for user-visible changes.

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (`fix: ...`, `feat: ...`); CI checks them.
