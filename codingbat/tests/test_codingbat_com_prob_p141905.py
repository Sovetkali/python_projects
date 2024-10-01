import pytest
from ..codingbat_com_prob_p141905 import sum_double

@pytest.mark.parametrize("a, b, result", [
    (2, 1, 3),
    (2, 2, 8)
    ])
def test_sum_double(a, b, result):
    assert sum_double(a, b) == result