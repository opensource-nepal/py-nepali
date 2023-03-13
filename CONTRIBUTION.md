# How to contribute

## Creating a Separate virtualenv

Before you contribute on this project you need to create a new separate [virtualenv](https://docs.python.org/3/library/venv.html).
Here is one example.

```bash
python -m venv .env
source .env/bin/activate
```

## Dependencies

We have listed all the dependencies in the `requirements.txt` files.

To install dependencies and prepare [`pre-commit`](https://pre-commit.com/) hooks you would need to run `install` command:

```bash
make install
```

## Codestyle

A `.editorconfig` is available to maintain the coding style. You can also use `black` for autoformatting.

```bash
black your-file-to-format.py
```

## Unitest

Run the unittest using the below command:

```bash
make test
```

### Coverage Report

To run the coverage report:

```bash
make coverage
```

To generate HTML coverage report

```bash
make coverage-html
```

### Before submitting

Before submitting your code please do the following steps:

1. Add any changes you want
1. Add tests for the new changes
1. Update the `CHANGELOG.md` file if necessary
1. Edit documentation if you have changed something significant
1. Run `black .` to format your changes.

## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
