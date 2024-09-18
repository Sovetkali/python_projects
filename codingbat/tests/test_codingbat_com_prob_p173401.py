import pytest
from ..codingbat_com_prob_p173401 import sleep_in

@pytest.mark.parametrize("weekday, vacation, result", [
    (False, False, True),
    (True, False, False),
    (False, True, True),
    (True, True, True)
    ])
def test_sleep_in(weekday, vacation, result):
    assert sleep_in(False, False) is True