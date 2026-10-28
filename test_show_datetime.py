from datetime import datetime

from show_datetime import format_datetime


def test_format_datetime():
    dt = datetime(2026, 8, 11, 9, 30, 5)
    assert format_datetime(dt) == "2026-08-11 09:30:05"
