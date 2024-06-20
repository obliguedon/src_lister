from files_lister.template_utils import extractor
import pytest
import pathlib
import os
import random
from datas import results

def test_correct_keys():
    good_keys_input = "./datas/good_keys.txt"
    abs_good_keys_input= pathlib.Path(os.path.join(os.path.dirname(__file__), good_keys_input)).resolve()
    with open(abs_good_keys_input, 'r') as file:
        input = file.read()

    result = extractor.get_all_params(input)
    assert results.good_keys.keys() == result.keys(), f"the extracted keys should have been {results.good_keys.keys()} but was {result.keys()}"

    for item, match in result.items():
        for var in results.good_keys[item]:
            assert match.group(var) == results.good_keys[item][var], f"extracted value for result[\"{item}\"][\"{var}\"] should have been {results.good_keys[item][var]}, but was {match.group(var)}"

def test_bad_template_exeption_wrong_type():
    with pytest.raises(TypeError):
        extractor.get_all_params(random.randint()) # int