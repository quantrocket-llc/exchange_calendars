from datetime import time
from .exchange_calendar_cmes import CMESExchangeCalendar


class CBOTExchangeCalendar(CMESExchangeCalendar):
    """
    Exchange calendar for the Chicago Board of Trade (CBOT).
    CBOT is owned and operated by CME Group and follows the CME
    holiday schedule.

    Open Time: 7:00 PM, America/Chicago
    Close Time: 1:20 PM, America/Chicago

    Trading break: 7:45 - 8:30 AM
    """

    name = "CBOT"
    open_times = ((None, time(19)),)
    close_times = ((None, time(13, 20)),)

    break_start_times = (
        (None, time(7, 45)),
    )
    break_end_times = (
        (None, time(8, 30)),
    )
