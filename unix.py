import datetime

def get_last_month_first_day_unix():
    today = datetime.datetime.today()
    first_day_current_month = today.replace(day=1)
    first_day_last_month = first_day_current_month - datetime.timedelta(days=1)
    first_day_last_month = first_day_last_month.replace(day=1)
    unix_timestamp = int(first_day_last_month.timestamp())
    return unix_timestamp