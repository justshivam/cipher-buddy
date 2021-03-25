from datetime import datetime, date


def get_timestamp():
    now = datetime.now()
    today = date.today()

    current_time = now.strftime('%H:%M:%S')
    d = today.strftime('%B, %d, %Y ')
    return f'{d}- {current_time}'
