PERIODS = (
    ("year", "y", 60 * 60 * 24 * 365 * 1000),
    ("month", "M", 60 * 60 * 24 * 30 * 1000),
    ("week", "M", 60 * 60 * 24 * 7 * 1000),
    ("day", "d", 60 * 60 * 24 * 1000),
    ("hour", "h", 60 * 60 * 1000),
    ("minute", "m", 60 * 1000),
    ("second", "s", 1000),
    ("millisecond", "ms", 1),
)


def strfdelta(duration, long=False):
    seconds = int(duration.total_seconds() * 1000)
    strings = []
    for period_name, period_short, period_seconds in PERIODS:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            if long:
                has_s = "s" if period_value > 1 else ""
                strings.append(f"{period_value} {period_name}{has_s}")
            else:
                strings.append(f"{period_value}{period_short}")

    return " ".join(strings)
