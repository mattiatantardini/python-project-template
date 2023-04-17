# Testing with `pytest`

## Write a test
Create a new script inside the `test` directory. The script name must start with `test_` or end with `_test.py`. Write test functions inside (you can optionally mark them with the `@pytest.mark` decorator).

## Run tests
From outside the test folder run:
```
pytest test
```
[Docs](https://docs.pytest.org/en/latest/explanation/goodpractices.html#conventions-for-python-test-discovery) with more details about tests are discovered.
