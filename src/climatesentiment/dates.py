
import datetime

def _to_timestamp(date: str) -> int:
    """
    Convert a date string to a timestamp.
    
    Args:
        date (str): Date string in the format 'YYYY-MM-DD'.
    
    Returns:
        int: Timestamp in seconds since epoch.
    """
    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    return int(dt.timestamp())