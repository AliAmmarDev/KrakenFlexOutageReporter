from datetime import datetime
from datetime import timezone

def convert_string_to_datetime(date_time_string: str) -> datetime:
    """
    Converts date string into datetime object.

    Parameters:
    date_time_string (str): string representing date.

    Returns:
    date_time_object (datetime): Datetime object.

    """

    date_time_string = date_time_string.replace("Z", "+00:00")
    try:
        date_time_object = datetime.fromisoformat(date_time_string).astimezone(timezone.utc)
        return date_time_object
    except ValueError:
        raise Exception(f"Invalid date provided: {date_time_string}")
