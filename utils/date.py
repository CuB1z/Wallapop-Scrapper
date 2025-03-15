from datetime import datetime, timedelta, timezone

def get_current_time(offest_hours: int = 0) -> datetime:
    tz = timezone(timedelta(hours=offest_hours))
    return datetime.now(tz).strftime("%d-%m-%Y %H:%M:%S")