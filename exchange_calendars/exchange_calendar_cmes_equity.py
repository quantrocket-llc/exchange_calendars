from datetime import time

from .exchange_calendar_cmes import CMESExchangeCalendar


class CMESEquityExchangeCalendar(CMESExchangeCalendar):
    """
    Exchange calendar for Equity Index products on the
    Chicago Mercantile Exchange (CMES).

    Open Time: 5:00 PM, America/Chicago
    Close Time: 4:00 PM, America/Chicago

    Trading Break: 3:15 - 3:30 PM
    """

    name = "CME_EQUITY"
    open_times = ((None, time(17)),)
    close_times = ((None, time(16)),)

    break_start_times = (
        (None, time(15, 15)),
    )
    break_end_times = (
        (None, time(15, 30)),
    )
