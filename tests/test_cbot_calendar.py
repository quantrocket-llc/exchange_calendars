import pytest

from exchange_calendars.exchange_calendar_cbot import CBOTExchangeCalendar
from .test_cmes_calendar import TestCMESCalendar


class CBOTCalendarTestCase(TestCMESCalendar):

    @pytest.fixture(scope="class")
    def calendar_cls(self):
        yield CBOTExchangeCalendar

    @pytest.fixture
    def max_session_hours(self):
        yield 18 + (1 / 3)
