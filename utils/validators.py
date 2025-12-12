import datetime


def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_future_date(date_string):
    if not is_valid_date(date_string):
        return False
    return datetime.datetime.strptime(date_string, "%Y-%m-%d") > datetime.datetime.now()


def is_valid_national_id(national_id):
    return national_id.isdigit() and len(national_id) == 10
