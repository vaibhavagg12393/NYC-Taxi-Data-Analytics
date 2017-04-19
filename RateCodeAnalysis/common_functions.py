import datetime

def convert_str_to_date(date_str):
    date_obj = None
    try:
        date_obj = datetime.datetime.strptime(date_str,'%Y-%m-%d %H:%M:%S')
    except Exception:
        pass
    return date_obj

def is_weekend(date_obj):
    return date_obj.weekday==5 or date_obj.weekday==6
