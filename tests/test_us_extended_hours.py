import pytest

from exchange_calendars.exchange_calendar_us_extended_hours import USExtendedHoursExchangeCalendar
from .test_xnys_calendar import TestXNYSCalendar


class USExtendedHoursCalendarTestCase(TestXNYSCalendar):

    @pytest.fixture(scope="class")
    def calendar_cls(self):
        yield USExtendedHoursExchangeCalendar

    @pytest.fixture
    def max_session_hours(self):
        yield 16
