import pytest
from gendiff import generate_diff
import os


P1_JSON = 'tests/fixtures/tree1.json'
P2_JSON = 'tests/fixtures/tree2.json'

P1_YAML = 'tests/fixtures/tree1.yml'
P2_YAML = 'tests/fixtures/tree2.yml'

PATH_STYLISH = 'tests/fixtures/check_stylish.txt'
PATH_PLAIN = 'tests/fixtures/check_plain.txt'
PATH_JSON = 'tests/fixtures/check_json.txt'
PATH_IDENTICAL_FILES = 'tests/fixtures/check_identical_files.txt'

OPTIONS = [(P1_JSON, P2_JSON, 'stylish', PATH_STYLISH),
           (P1_JSON, P2_JSON, 'plain', PATH_PLAIN),
           (P1_JSON, P2_JSON, 'json', PATH_JSON),
           (P1_YAML, P2_YAML, 'stylish', PATH_STYLISH),
           (P1_YAML, P2_YAML, 'plain', PATH_PLAIN),
           (P1_YAML, P2_YAML, 'json', PATH_JSON),
           (P1_JSON, P1_JSON, 'stylish', PATH_IDENTICAL_FILES),
           ]


@pytest.mark.parametrize("path1, path2, format, path_check_file", OPTIONS)
def test_generate_diff(path1, path2, format, path_check_file):
    res = generate_diff(path1, path2, format)

    with open(path_check_file) as check_file:
        assert res == check_file.read()