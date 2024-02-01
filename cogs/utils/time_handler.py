import datetime as dt
from dateutil import tz

def calculate_sprint(arg):
    try:
        time = None
        duration = 20

        if "à" in arg:
            pos = arg.index("à")
            time = int(arg[pos+1])
        else:
            time = dt.datetime.now().minute + 1

        if "pour" in arg:
            pos_p = arg.index("pour")
            duration = int(arg[pos_p+1])

        if time > 59 or duration > 59:
            return 0
        
        return time, duration

    except:
        return 0

def return_delays(msg):
    """
    Take the pair of numbers returned to calculate_sprint
    and turn them into the length of time to wait.
    """
    time_pair = calculate_sprint(msg)

    if time_pair == 0:
        return 0 
    
    start = time_pair[0]
    duration = time_pair[1]

    now = dt.datetime.now()

    if now.minute > start:
        return 0

    start_time = now.replace(minute=start)
    end_time = start_time + dt.timedelta(minutes=duration)

    delay_start = start_time - now
    delay_end = end_time - start_time
    return (delay_start.total_seconds(), delay_end.total_seconds(), start_time)


def set_reminder_delay(specific_time):
    try:
        is_french = tz.gettz('Europe/Paris')
        fr_timezone = dt.datetime.now()
        fr_timezone = fr_timezone.astimezone(is_french)

        new_date = fr_timezone.replace(
            hour=int(specific_time[:2]),
            minute=int(specific_time[-2:])
        )

        if new_date < fr_timezone:
            new_date = new_date + dt.timedelta(hours=24)
            
        difference = new_date - fr_timezone
        wait_for = difference.total_seconds()

        return wait_for
    except:
        return False
    
def reminder_format(message):
    time = message[-5:]
    time_reminder = set_reminder_delay(time)

    if not time_reminder:
        return False
    else:
        reminder = message[:-5]
        reminder = message.split()
        reminder.pop(0)
        reminder = " ".join(reminder)

        return [reminder, time_reminder]
