from math import floor


def humanize_time_difference(now, then):
    if then:
        dt = now - then

        if dt.days:
            elapsed = dt.days
            time_format = 'day'
        elif dt.seconds >= 3600:
            elapsed = floor(dt.seconds / 3600)
            time_format = 'hour'
        elif dt.seconds >= 60:
            elapsed = floor(dt.seconds / 60)
            time_format = 'minute'
        else:
            elapsed = dt.seconds
            time_format = 'second'
    else:
        raise ValueError("Must supply otherdate or offset (from now)")

    return '{} {}{} ago'.format(elapsed, time_format, '' if elapsed == 1 else 's')
