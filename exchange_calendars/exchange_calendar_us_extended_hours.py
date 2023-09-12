from datetime import time
from exchange_calendars.exchange_calendar_xnys import XNYSExchangeCalendar


class USExtendedHoursExchangeCalendar(XNYSExchangeCalendar):
    """
    A calendar for extended hours which runs from 4 AM to 8 PM.
    """

    name = "us_extended_hours"

    open_times = ((None, time(4)),)
    close_times = ((None, time(20)),)

    regular_early_close = time(17)
