import pytest

from exchange_calendars.exchange_calendar_cmes_equity_liquid import CMESEquityLiquidHoursExchangeCalendar
from .test_cmes_calendar import TestCMESCalendar


class CMESEquityLiquidHoursCalendarTestCase(TestCMESCalendar):

    @pytest.fixture(scope="class")
    def calendar_cls(self):
        yield CMESEquityLiquidHoursExchangeCalendar

    @pytest.fixture
    def max_session_hours(self):
        yield 7.5
