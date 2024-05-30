import pytest

from python_learning.sample import ADemoClass

@pytest.mark.parametrize("values_and_response", [(1, 2), (2, 4), (3, 6)])
def test_sample_method(
    values_and_response: int
):
    sample_class = ADemoClass()
    value_to_operate, expected_response = values_and_response
    assert sample_class.multiply_base_number_by_two(value_to_operate) == expected_response