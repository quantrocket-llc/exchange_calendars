from datetime import time

from .exchange_calendar_cmes_equity import CMESEquityExchangeCalendar


class CMESEquityLiquidHoursExchangeCalendar(CMESEquityExchangeCalendar):
    """
    Exchange calendar for liquid hours for Equity Index products on the
    Chicago Mercantile Exchange (CMES). Liquid hours is based on IBKR's
    definition and corresponds to the times for which IBKR returns historical
    data when the `outsideRth` flag is omitted.

    Open Time: 8:30 AM, America/Chicago
    Close Time: 4:00 PM, America/Chicago

    Trading Break: 3:15 - 3:30 PM
    """

    name = "CME_EQUITY_LIQUID"
    open_times = ((None, time(8, 30)),)
    close_times = ((None, time(16)),)

    @property
    def open_offset(self):
        return 0

    break_start_times = (
        (None, time(15, 15)),
    )
    break_end_times = (
        (None, time(15, 30)),
    )
