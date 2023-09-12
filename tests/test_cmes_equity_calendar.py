import pytest

from exchange_calendars.exchange_calendar_cmes_equity import CMESEquityExchangeCalendar
from .test_cmes_calendar import TestCMESCalendar


class CMESEquityCalendarTestCase(TestCMESCalendar):

    @pytest.fixture(scope="class")
    def calendar_cls(self):
        yield CMESEquityExchangeCalendar

    @pytest.fixture
    def max_session_hours(self):
        yield 23
